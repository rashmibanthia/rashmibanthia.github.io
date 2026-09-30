# Rashmi Banthia — portfolio refresh

A responsive Hugo portfolio built on the existing `rashmibanthia.github.io` source, with no framework migration. The original project source and theme are retained. GitHub Pages publishes the generated `docs/` directory on `main` at https://rashmibanthia.github.io/.

## Local preview

```sh
./scripts/preview.sh
```

Open **http://localhost:1313/**. The preview binds only to loopback and renders into memory. File polling keeps edits visible even when macOS file notifications are missed. Set `PORT=1314` if 1313 is already in use.

The scripts use the downloaded Hugo binary at `../bin/hugo`, then fall back to `hugo` on PATH. To use a different binary, set `HUGO_BIN=/absolute/path/to/hugo`. Tested with Hugo 0.128.2 on macOS arm64.

## Build and check

```sh
./scripts/build.sh
python3 scripts/check_site.py
node --check static/js/portfolio.js
```

Build output is `../preview/`, deliberately separate from the tracked deployment output in `docs/`. Local checks verify all generated internal links/assets/anchors, exclusion of retired archive pages, the résumé PDF, and the explicit BirdCLEF staging label.

## Editing

- `layouts/index.html`: homepage sections and BirdCLEF feature.
- `data/selected.json`: curated project cards and writeup links.
- `static/css/portfolio.css`: responsive design; reduced-motion support.
- `static/js/portfolio.js`: mobile navigation, including Escape handling.
- `static/images/`: original abstract SVG illustrations, not measured scientific plots.
- `static/files/Rashmi-Banthia-Resume.pdf`: unchanged copy of the supplied résumé.
- `content/project/`: original nine project descriptions, unchanged and excluded from builds by `ignoreFiles` in `config.toml`. Remove that exclusion to restore the archive.

DM Sans loads from Google Fonts with a system sans-serif fallback. No analytics, client framework, or third-party script is required.

## Publishing

The existing GitHub Pages source is **main /docs**, with no custom domain. The historical `gh-pages` branch is not the publishing source. Do not change custom-domain settings or redirect other domains as part of this site.

After reviewing changes and obtaining publishing approval:

```sh
BUILD_DESTINATION=docs ./scripts/build.sh
python3 scripts/check_site.py docs
```

Commit the source changes and rebuilt `docs/` together, then push to `main`. GitHub Pages deploys that directory. The maintained `.github/workflows/gh-pages.yml` builds with Hugo 0.128.2 on Ubuntu 24.04, checks links and JavaScript, and verifies that `docs/` matches a clean build. It does not push another branch.

The old `content/project/` files remain available in source/history but are excluded from generated output. Local preview and build checks alone do not confirm production deployment success.
