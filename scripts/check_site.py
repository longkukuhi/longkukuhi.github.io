"""Check same-site links and media in a generated Jekyll site, without network I/O."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for name in ("href", "src", "poster"):
            if attrs.get(name):
                self.urls.append(attrs[name])
        if tag == "object" and attrs.get("data"):
            self.urls.append(attrs["data"])
        srcset = attrs.get("srcset", "")
        if srcset and not srcset.startswith("data:"):
            self.urls.extend(item.strip().split()[0] for item in srcset.split(",") if item.strip())


def check_site(root, site_url):
    root = Path(root).resolve()
    site_url = site_url.rstrip("/") + "/"
    origin = urlsplit(site_url)
    prefix = unquote(origin.path)
    files = sorted(root.rglob("*.html"))
    if not (root / "index.html").is_file():
        raise ValueError(f"No generated homepage at {root / 'index.html'}")
    errors = set()
    checked = 0
    for page in files:
        relative = page.relative_to(root).as_posix()
        if any(part.startswith(".") for part in page.relative_to(root).parts):
            continue
        checked += 1
        parser = References()
        parser.feed(page.read_text(encoding="utf-8"))
        page_url = urljoin(site_url, relative.removesuffix("index.html"))
        for reference in parser.urls:
            url = urlsplit(urljoin(page_url, reference))
            if url.scheme not in ("http", "https") or url.netloc != origin.netloc:
                continue
            path = unquote(url.path)
            if not path.startswith(prefix):
                errors.add((relative, reference))
                continue
            target = (root / path[len(prefix):]).resolve()
            if not target.is_relative_to(root) or not (
                target.is_file() or (target / "index.html").is_file()
            ):
                errors.add((relative, reference))
    return checked, sorted(errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--site-url", required=True)
    args = parser.parse_args()
    try:
        count, errors = check_site(args.directory, args.site_url)
    except ValueError as error:
        parser.error(str(error))
    for page, reference in errors:
        print(f"MISSING {page}: {reference}")
    print(f"Checked {count} HTML files; {len(errors)} broken local references.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
