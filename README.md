# indycocreator.com

The public Indy CoCreator website, served by Cloudflare from the `main` branch of this repo.

**These files are generated. Don't edit the HTML here.** Every page is exported from the `bharp0614/UIGEN` repo by `npm run export:site -- <path to this repo>`, and the next export overwrites whatever is here. `export-info.json` records which UIGEN commit the files came from.

| Path | What it is |
|---|---|
| `index.html`, `about/`, `services/`, `pricing/`, `faq/`, `contact/` | Agency site pages |
| `portfolio/` | Portfolio: live client sites link to their own domains; demos are hosted at `portfolio/<slug>/` |
| `_next/static/` | JavaScript, CSS and fonts the pages load |
| `portfolio/*.png`, `demos/`, `clients/`, `images/` | Images |
| `404.html` | Page shown for unknown URLs |
| `templates/redeveloper/` | The earlier "Redeveloper" HTML template, kept for reference. Not linked from the site. |

How to publish an update: see `docs/PROCESS-AND-SETUP.md` §7A in UIGEN.
