"""This module is called after project is created."""
from typing import List

import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.package_name }}"
PROJECT_MODULE = "{{ cookiecutter.package_name.lower().replace(' ', '_').replace('-', '_') }}"
CREATE_EXAMPLE_TEMPLATE = "{{ cookiecutter.create_example_template }}"

# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"

# Values to generate github repository
GITHUB_USER = "{{ cookiecutter.github_name }}"


def remove_unused_files(directory: Path, module_name: str, need_to_remove_cli: bool) -> None:
    """Remove unused files.

    Args:
        directory: path to the project directory
        module_name: project module name
        need_to_remove_cli: flag for removing CLI related files
    """
    files_to_delete: List[Path] = []

    def _cli_specific_files() -> List[Path]:
        return [directory / module_name / "__main__.py"]

    if need_to_remove_cli:
        files_to_delete.extend(_cli_specific_files())

    for path in files_to_delete:
        path.unlink()


def print_futher_instuctions(package_name: str, github: str) -> None:
    """Show user what to do next after project creation.

    Args:
        package_name: current project name
        github: GitHub username
    """
    message = f"""
    Your project {package_name} is created.

    1) Now you can start working on it:

        $ cd {package_name} && git init

    2) If you don't have Poetry installed run:

        $ make poetry-download

    2) install package in developer mode

        $ pip install -e .[dev]

    3) Upload initial code to GitHub:

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin https://github.com/{github}/{package_name}.git
        $ git push -u origin main
    """
    print(textwrap.dedent(message))


def main() -> None:
    # remove_unused_files(
    #     directory=PROJECT_DIRECTORY,
    #     module_name=PROJECT_MODULE,
    #     need_to_remove_cli=CREATE_EXAMPLE_TEMPLATE != "cli",
    # )
    print_futher_instuctions(package_name=PROJECT_NAME, github=GITHUB_USER)


if __name__ == "__main__":
    main()
