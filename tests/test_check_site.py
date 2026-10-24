import tempfile
import unittest
from pathlib import Path

from scripts.check_site import check_site


class SiteLinksTest(unittest.TestCase):
    def test_detects_missing_pdf_and_responsive_images(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text(
                '<a href="/assets/cv.pdf">CV</a>'
                '<source srcset="/assets/photo-480.webp 480w, /assets/photo-800.webp 800w">'
            )
            count, errors = check_site(root, "https://example.com/")
            self.assertEqual(count, 1)
            self.assertEqual({url for _, url in errors}, {
                "/assets/cv.pdf", "/assets/photo-480.webp", "/assets/photo-800.webp"
            })

    def test_resolves_nested_pages_queries_and_encoded_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "cv").mkdir()
            (root / "assets").mkdir()
            (root / "assets" / "my cv.pdf").touch()
            (root / "index.html").write_text('<a href="/site/cv/">CV</a>')
            (root / "cv" / "index.html").write_text(
                '<a href="../assets/my%20cv.pdf?v=2#page=1">PDF</a>'
                '<a href="https://example.com/site/">Home</a>'
                '<a href="https://other.example/">External</a>'
                '<a href="mailto:person@example.com">Email</a>'
            )
            self.assertEqual(check_site(root, "https://example.com/site/"), (2, []))

    def test_empty_site_does_not_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                check_site(directory, "https://example.com/")


if __name__ == "__main__":
    unittest.main()
