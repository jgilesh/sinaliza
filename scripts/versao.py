#!/usr/bin/env python3
"""Stamps sw.js with a version made from the content of every file the site serves.

Run before every commit that changes the site. A new version makes the service worker
re-cache everything, and open pages reload once to show the update.

    python3 scripts/versao.py           # update sw.js
    python3 scripts/versao.py --check   # exit 1 if sw.js is out of date
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVED = ['index.html', 'manifest.webmanifest', 'css', 'js', 'data', 'media', 'icons']


def site_hash():
    h = hashlib.sha1()
    for entry in SERVED:
        path = ROOT / entry
        files = sorted(p for p in path.rglob('*') if p.is_file()) if path.is_dir() else [path]
        for f in files:
            if f.name.startswith('.'):
                continue
            h.update(str(f.relative_to(ROOT)).encode())
            h.update(f.read_bytes())
    return h.hexdigest()[:10]


def main():
    sw = ROOT / 'sw.js'
    text = sw.read_text(encoding='utf-8')
    version = f'sinais-{site_hash()}'
    new = re.sub(r"const CACHE = '[^']*';", f"const CACHE = '{version}';", text, count=1)
    if '--check' in sys.argv:
        if new != text:
            print(f'sw.js is out of date: run python3 scripts/versao.py ({version})')
            sys.exit(1)
        print(f'sw.js ok ({version})')
        return
    sw.write_text(new, encoding='utf-8')
    print(version)


if __name__ == '__main__':
    main()
