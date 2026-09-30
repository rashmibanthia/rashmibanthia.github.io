"""Validate the built site's local navigation and exclusion of retired project pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
root = Path(sys.argv[1] if len(sys.argv) > 1 else '../preview').resolve()
class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(); self.ids = set(); self.links = []; self.h1 = 0; self.errors = []
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.errors.append('duplicate id: ' + a['id'])
            self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        for attr in ('href', 'src'):
            if attr in a: self.links.append(a[attr])
pages = {p: Page(p.read_text()) for p in root.rglob('*.html')}
errors = []
for path, page in pages.items():
    for e in page.errors: errors.append(f'{path.relative_to(root)}: {e}')
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        target = root / unquote(url.path.lstrip('/')) if url.path.startswith('/') else path.parent / unquote(url.path)
        if not url.path: target = path
        if target.is_dir(): target /= 'index.html'
        if not target.exists(): errors.append(f'{path.relative_to(root)}: missing {link}')
        elif url.fragment and target in pages and url.fragment not in pages[target].ids:
            errors.append(f'{path.relative_to(root)}: missing anchor {link}')
assert not list((root/'project').rglob('*.*')), 'Retired archive files remain in generated output'
for path in root.rglob('*'):
    if path.is_file() and path.suffix in {'.html', '.xml'}:
        assert '/project/' not in path.read_text(), f'Archive reference remains: {path}'
assert 'slc9cYjob4g' not in (root/'index.html').read_text(), 'Retired H2O talk remains'
assert pages[root/'index.html'].h1 == 1, 'Homepage must have one H1'
assert (root/'files/Rashmi-Banthia-Resume.pdf').read_bytes().startswith(b'%PDF'), 'Resume is not a PDF'
assert 'Working note' in (root/'index.html').read_text() and 'in staging' in (root/'index.html').read_text()
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {len(pages)} HTML pages; all local assets, links, and anchors resolve; retired archive and H2O entry excluded; resume and staging label verified.')
