"""Test runner."""

import pathlib

import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session(python=["3.9", "3.8", "3.7"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("coverage", "run")


@nox.session
def coverage_report(session):
    session.install("coverage[toml]")
    session.run("coverage", "combine")
    session.run("coverage", "html")
    session.run("coverage", "report")


@nox.session
def lint(session):
    node_path = pathlib.Path.cwd() / "node_modules/.bin"
    pyright = pathlib.Path(session.bin) / "pyright"
    pyright.symlink_to(node_path / "pyright")
    session.run("poetry", "install", "-E", "lint", external=True)
    session.run("mypy", "--disallow-untyped-defs", "-p", "enerator")
    session.run("pyright", external=True)
    session.run("flake8", "src/enerator", "tests")
