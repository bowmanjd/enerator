"""Parse a file, generating output."""

import pathlib

import frontmatter  # type: ignore

from . import parse


def parse_file(filepath: pathlib.Path) -> str:
    """
    Convert a frontmatter + Markdown file to HTML.

    Args:
        filepath: path to file

    Returns:
        HTML
    """
    article = frontmatter.load(filepath)
    return parse.md_highlight_and_parse(article.content)
