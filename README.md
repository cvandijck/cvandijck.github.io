# Website

Welcome to the website of Christophe Van Dijck.

Feel free to browse around in the source code, but you get the best experience at [www.christophevandijck.be](https://www.christophevandijck.be).

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) 12.13 or higher (required by TailwindCSS)

### Install

```bash
npm install
```

### Develop

Runs a TailwindCSS/PostCSS watcher and a [BrowserSync](https://www.browsersync.io/) live-reload server:

```bash
npm run develop
```

### Build

Compiles and minifies the production CSS bundle into `assets/styles/main.min.css`:

```bash
npm run build
```

### Format

Formats all HTML files with Prettier:

```bash
npm run format
```

### Pre-commit hook

A [Husky](https://typicode.github.io/husky/) `pre-commit` hook runs `npm run build` automatically before each commit, to catch CSS build errors early. It's installed automatically via `npm install` (the `prepare` script).

## Project Structure

```
├── index.html            # Homepage
├── 404.html               # Custom 404 page
├── CNAME                  # Custom domain config for GitHub Pages
├── assets/
│   ├── img/               # Images and illustrations
│   ├── js/
│   │   └── main.js        # Site scripts
│   └── styles/
│       ├── main.css       # Source styles (Tailwind + custom)
│       └── main.min.css   # Compiled/minified CSS (generated, do not edit)
├── projects/              # Individual project pages (e.g. projects/phd)
├── tailwind.config.js     # TailwindCSS configuration
├── postcss.config.js      # PostCSS plugins (Tailwind, autoprefixer, cssnano)
├── browser-sync-config.js # BrowserSync live-reload configuration
└── package.json           # Scripts and dependencies
```

Styles are authored in `assets/styles/main.css` and compiled to `assets/styles/main.min.css` via the `css` npm script — edit the source file, not the generated one.

The site is built with the [Atom](https://redpixelthemes.com/templates/atom/) TailwindCSS template.

## Built With

- [TailwindCSS](https://tailwindcss.com/): utility-first CSS framework.
- [Alpine.js](https://github.com/alpinejs/alpine) & [Alpine Collective Toolkit](https://github.com/alpine-collective/toolkit): reactive/declarative behavior without a heavy framework.
- [Boxicons](https://boxicons.com/): icon set.
- [Highlight.js](https://highlightjs.org/): code syntax highlighting (Atom Dark theme).
- Tailwind plugins: [Forms](https://github.com/tailwindlabs/tailwindcss-forms), [Typography](https://github.com/tailwindlabs/tailwindcss-typography), [Aspect Ratio](https://github.com/tailwindlabs/tailwindcss-aspect-ratio).

## Continuous Integration

Two GitHub Actions workflows run automatically to help catch issues early:

- **CI** ([.github/workflows/ci.yml](.github/workflows/ci.yml)): installs dependencies, audits for known vulnerabilities, builds the CSS bundle and checks HTML formatting with Prettier on every push/PR to `main`.
- **Links** ([.github/workflows/links.yml](.github/workflows/links.yml)): scans HTML/Markdown files for broken links on every push/PR to `main` and on a weekly schedule.

## Acknowledgement
- Webdesign by [Atom](https://redpixelthemes.com/templates/atom/)
- Illustrations by [Storyset](https://storyset.com/idea)

