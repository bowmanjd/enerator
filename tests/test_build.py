"""Testing build functionality."""

import pathlib

from enerator.build import *

SRCDIR = pathlib.Path("tests/src")
HTML_TEMPLATE = pathlib.Path("tests/tpl/sample_template.html")


def test_render_to_md():
    result = render_from_file(MARKDOWN, MARKDOWN_TEMPLATE)
    assert "By Jonathan" in result.content
