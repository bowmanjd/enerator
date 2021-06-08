"""Testing templating and frontmatter."""

import pathlib

from enerator.template import render_from_file

MARKDOWN = pathlib.Path("tests/sample.md")
MARKDOWN_TEMPLATE = pathlib.Path("tests/sample_template.md")
HTML_TEMPLATE = pathlib.Path("tests/sample_template.html")


def test_render_to_md():
    result = render_from_file(MARKDOWN, MARKDOWN_TEMPLATE)
    assert "By Jonathan" in result.content


def test_render_to_html():
    result = render_from_file(MARKDOWN, HTML_TEMPLATE)
    assert result.content == pathlib.Path("tests/sample_output.html").read_text()
