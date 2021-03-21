"""Template rendering."""

import pathlib
import typing

import frontmatter  # type: ignore
from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader


class Page(typing.NamedTuple):
    """Container for content and metadata."""

    content: str
    data: dict


def render_from_file(
    file_path: pathlib.Path,
    template_path: pathlib.Path = None,
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
    template_path = template_path or pathlib.Path.cwd() / "templates"
    data = data or {}
    page = frontmatter.load(file_path)

    loaders = [
        DictLoader({"content": page.content}),
        FileSystemLoader(file_path.parent),
    ]
    if template_path.exists():
        loaders.append(FileSystemLoader(template_path.parent))

    loader = ChoiceLoader(loaders)
    template_env = Environment(loader=loader, autoescape=True)
    template = template_env.get_template(template_path.name)
    final_data = {**data, **page.metadata}
    return Page(template.render(**final_data), final_data)
