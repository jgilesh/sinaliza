// Keeps the app usable offline and fast on a weak signal (interpreters often work in places
// like that). Drawings: cache first. Everything else: answer from the cache right away and
// refresh it in the background (stale-while-revalidate). The page itself: network first,
// with a short timeout, so a deploy shows up on the next visit.
// CACHE is stamped by scripts/versao.py from the content of the site: any change makes a new
// version, install re-caches everything and open pages reload once.
const CACHE = 'sinais-abf9f01a73';
const CORE = [
  './', 'index.html', 'css/app.css', 'js/app.js', 'js/search.js', 'data/sinais.json',
  'manifest.webmanifest', 'icons/icon.svg', 'icons/apple-touch-icon.png',
];
const PAGE_TIMEOUT_MS = 2500;
const APP_PATH = new URL('./', self.location).pathname;

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    // 'reload' skips the browser's HTTP cache, so a new version never stores old files.
    await cache.addAll(CORE.map(url => new Request(url, { cache: 'reload' })));
    // Every drawing listed in the data (read from the copy just cached), so all signs work
    // offline from the first visit. One missing file must not cancel offline mode for the rest.
    const res = await cache.match('data/sinais.json');
    if (res) {
      const data = await res.json();
      const media = data.signs.flatMap(s => [s.image, s.poster, s.handshapeImage]).filter(Boolean);
      const results = await Promise.allSettled(media.map(url => cache.add(new Request(url, { cache: 'reload' }))));
      results.forEach((r, i) => r.status === 'rejected' && console.warn('SW: not cached', media[i]));
    }
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);
  if (request.method !== 'GET' || url.origin !== self.location.origin) return;
  if (request.mode === 'navigate') {
    // Only the app's own page is cached; other pages on the site (e.g. tests/) are left alone.
    if (url.pathname === APP_PATH || url.pathname === `${APP_PATH}index.html`) event.respondWith(pageFirst(event, request));
  } else if (url.pathname.includes('/media/')) {
    event.respondWith(cacheFirst(request));
  } else {
    event.respondWith(staleWhileRevalidate(event, request));
  }
});

// Cache key without the query string, so "?t=1" variants don't pile up.
function keyOf(request) {
  const url = new URL(request.url);
  url.search = '';
  return url.href;
}

async function cacheFirst(request) {
  const cache = await caches.open(CACHE);
  const cached = await cache.match(keyOf(request));
  if (cached) return cached;
  const response = await fetch(request);
  if (response.ok) cache.put(keyOf(request), response.clone());
  return response;
}

async function staleWhileRevalidate(event, request) {
  const cache = await caches.open(CACHE);
  const cached = await cache.match(keyOf(request));
  const network = fetch(request).then(response => {
    if (response.ok) cache.put(keyOf(request), response.clone());
    return response;
  });
  event.waitUntil(network.catch(() => {}));
  return cached ?? network;
}

async function pageFirst(event, request) {
  const cache = await caches.open(CACHE);
  const network = fetch(request).then(response => {
    if (response.ok) cache.put('index.html', response.clone());
    return response;
  });
  event.waitUntil(network.catch(() => {})); // keep refreshing the copy even after a timeout
  const timeout = new Promise(resolve => setTimeout(resolve, PAGE_TIMEOUT_MS, null));
  try {
    const response = await Promise.race([network, timeout]);
    if (response && response.ok) return response;
  } catch {
    // offline: fall through to the cache
  }
  return (await cache.match('index.html')) ?? network;
}
