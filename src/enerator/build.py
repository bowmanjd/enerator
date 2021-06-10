"""Build pages and structure."""

import pathlib
import typing

from . import template


def render_directory(
    directory: pathlib.Path,
    template_path: pathlib.Path,
    pattern: str = "**/*.md",
    data: typing.Mapping = None,
) -> typing.Iterator:
    """
    Render multiple files from directory.

    Args:
        directory: path to parent directory of files
        template_path: path to parent template file
        pattern: optional glob-style pattern
        data: dict of additional variables

    Yields:
        Page content and metadata

    """
    files = directory.glob(pattern)
    for result in render_files(template_path, files, data):
        yield result


def render_files(
    template_path: pathlib.Path,
    files: typing.Iterable[pathlib.Path],
    data: typing.Mapping = None,
) -> typing.Iterator:
    """
    Render multiple files.

    Args:
        template_path: path to parent template file
        files: iterable of paths to files with page content
        data: dict of additional variables

    Yields:
        Page content and metadata

    """
    for file_path in files:
        yield template.render_from_file(file_path, template_path, data)
