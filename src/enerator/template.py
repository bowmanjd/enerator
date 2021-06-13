"""Template rendering."""

import pathlib
import typing

import frontmatter  # type: ignore
from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader

from . import parse


class Page(typing.NamedTuple):
    """Container for content and metadata."""

    content: str
    data: dict
    source_path: pathlib.Path


def render_from_file(
    file_path: pathlib.Path,
    template_path: pathlib.Path,
    data: typing.Mapping = None,
) -> Page:
    """
    Render from template file.

    Args:
        file_path: path to file with page content
        template_path: path to parent template file
        data: dict of additional variables

    Returns:
        Page content and metadata

    """
    data = data or {}
    page = frontmatter.load(file_path)

    loaders = [
        DictLoader({"content": page.content}),
        FileSystemLoader([file_path.parent, template_path.parent]),
    ]

    loader = ChoiceLoader(loaders)
    template_env = Environment(loader=loader, autoescape=True)
    template_env.filters["markdown"] = parse.md_highlight_and_parse
    template = template_env.get_template(template_path.name)
    final_data = {**data, **page.metadata}
    rendered = template.render(**final_data)
    if template_path.suffix == ".html":
        rendered = parse.tidy_html(rendered)
    return Page(rendered, final_data, file_path)
