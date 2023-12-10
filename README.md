<!-- Banner -->
![alt Banner of the Weerlive package](https://raw.githubusercontent.com/klaasnicolaas/python-weerlive/main/assets/header_weerlive-min.png)

<!-- PROJECT SHIELDS -->
[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits-url]
[![PyPi Downloads][downloads-shield]][downloads-url]
[![GitHub Last Commit][last-commit-shield]][commits-url]
[![Open in Dev Containers][devcontainer-shield]][devcontainer]

[![Build Status][build-shield]][build-url]
[![Typing Status][typing-shield]][typing-url]
[![Maintainability][maintainability-shield]][maintainability-url]
[![Code Coverage][codecov-shield]][codecov-url]


Asynchronous Python client for Weerlive API.

## About

A Python package with which you can retrieve current weather data from the [KNMI][knmi] via the [Weerlive][weerlive] API.

## Installation

```bash
pip install weerlive
```

## Data

It's a very extensive weather model, the list of which is too large to describe here, so it is best to [read here](./src/weerlive/models.py) which data you can request using this package.

## Example

```python
import asyncio

from weerlive import Weerlive


async def main() -> None:
    """Show example on using this package."""
    async with Weerlive(
        api_key="API_KEY",
        longitude=52.1009166,
        latitude=5.6462914,
    ) as client:
        weather = await client.weather()
        print(weather)


if __name__ == "__main__":
    asyncio.run(main())
```

### Class Parameters

| Parameter | value Type | Description |
| :-------- | :--------- | :---------- |
| `api_key` | `str` | The API key to use for the connection (Request API key [here](https://weerlive.nl/delen.php)). |
| `latitude` | `float` | The latitude of the location to retrieve the weather data for. |
| `longitude` | `float` | The longitude of the location to retrieve the weather data for. |

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

The simplest way to begin is by utilizing the [Dev Container][devcontainer]
feature of Visual Studio Code or by opening a CodeSpace directly on GitHub.
By clicking the button below you immediately start a Dev Container in Visual Studio Code.

[![Open in Dev Containers][devcontainer-shield]][devcontainer]

This Python project relies on [Poetry][poetry] as its dependency manager,
providing comprehensive management and control over project dependencies.

You need at least:

- Python 3.11+
- [Poetry][poetry-install]

Install all packages, including all development requirements:

```bash
poetry install
```

Poetry creates by default an virtual environment where it installs all
necessary pip packages, to enter or exit the venv run the following commands:

```bash
poetry shell
exit
```

Setup the pre-commit check, you must run this inside the virtual environment:

```bash
pre-commit install
```

*Now you're all set to get started!*

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

## License

MIT License

Copyright (c) 2023 Klaas Schoute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


<!-- LINKS FROM PLATFORM -->
[weerlive]: https://weerlive.nl
[knmi]: https://www.knmi.nl

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/klaasnicolaas/python-weerlive/actions/workflows/tests.yaml/badge.svg
[build-url]: https://github.com/klaasnicolaas/python-weerlive/actions/workflows/tests.yaml
[codecov-shield]: https://codecov.io/gh/klaasnicolaas/python-weerlive/branch/main/graph/badge.svg?token=3UTVTR785Y
[codecov-url]: https://codecov.io/gh/klaasnicolaas/python-weerlive
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/python-weerlive.svg
[commits-url]: https://github.com/klaasnicolaas/python-weerlive/commits/main
[devcontainer-shield]: https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode
[devcontainer]: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/klaasnicolaas/python-weerlive
[downloads-shield]: https://img.shields.io/pypi/dm/weerlive
[downloads-url]: https://pypistats.org/packages/weerlive
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/python-weerlive.svg
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/python-weerlive.svg
[maintainability-shield]: https://api.codeclimate.com/v1/badges/dc7c4ef7ba9a00f11787/maintainability
[maintainability-url]: https://codeclimate.com/github/klaasnicolaas/python-weerlive/maintainability
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/weerlive/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/weerlive
[releases-shield]: https://img.shields.io/github/release/klaasnicolaas/python-weerlive.svg
[releases]: https://github.com/klaasnicolaas/python-weerlive/releases
[typing-shield]: https://github.com/klaasnicolaas/python-weerlive/actions/workflows/typing.yaml/badge.svg
[typing-url]: https://github.com/klaasnicolaas/python-weerlive/actions/workflows/typing.yaml

[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
