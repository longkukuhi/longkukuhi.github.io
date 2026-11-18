# Zijun Long · Academic website

Personal academic website for Zijun Long at Hunan University. The site presents research in multimodal retrieval, robotic perception and industrial visual analysis. [Visit the website](https://longkukuhi.github.io/) · [Browse publications](https://longkukuhi.github.io/publications/)

## Edit the site

| Content | Source |
| --- | --- |
| Homepage biography and profile | [About page](_pages/about.md) |
| Publications and selected papers on the homepage | [BibTeX entries](_bibliography/papers.bib) |
| News announcements | [News entries](_news/) |
| Project descriptions | [Project pages](_projects/) |
| Site identity, URL and navigation settings | [Jekyll configuration](_config.yml) and [pages](_pages/) |

For a new paper, add the BibTeX entry and set `selected={true}` if it should also appear on the homepage. The theme's publication formatting and other options are documented in the [customization guide](CUSTOMIZE.md).

## Preview and check a change

With Docker and Compose installed, run these commands from the repository root.

```sh
docker compose pull
docker compose up
```

Open <http://localhost:8080> and check the affected pages. Native Ruby setup and additional options are in the [installation guide](INSTALL.md). After Jekyll builds the site into `_site/`, the repository's checker validates same-site links and media references.

```sh
python3 -m unittest discover -s tests
python3 scripts/check_site.py _site --site-url https://longkukuhi.github.io/
```

The [deployment workflow](.github/workflows/deploy.yml) builds with Jekyll, checks the generated site, and publishes eligible changes through GitHub Pages.

## Theme and credits

The site uses [al-folio](https://github.com/alshedivat/al-folio), a Jekyll theme for academics. Its original design grew from [Lia Bogoev's **\*folio**](https://github.com/bogoli/-folio). See the [MIT license](LICENSE), [theme FAQ](FAQ.md) and [contributor guide](CONTRIBUTING.md).

### Upstream al-folio maintainers

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://maruan.alshedivat.com"><img src="https://avatars.githubusercontent.com/u/2126561?v=4" width="100px;" alt=""/><br /><sub><b>Maruan</b></sub></a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://rohandebsarkar.github.io"><img src="https://avatars.githubusercontent.com/u/50144004?v=4" width="100px;" alt=""/><br /><sub><b>Rohan Deb Sarkar</b></sub></a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://amirpourmand.ir"><img src="https://avatars.githubusercontent.com/u/32064808?v=4" width="100px;" alt=""/><br /><sub><b>Amir Pourmand</b></sub></a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://george-gca.github.io/"><img src="https://avatars.githubusercontent.com/u/31376482?v=4" width="100px;" alt=""/><br /><sub><b>George</b></sub></a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

### Upstream contributors

<a href="https://contrib.rocks">
  <img src="https://contrib.rocks/image?repo=alshedivat/al-folio" />
</a>
