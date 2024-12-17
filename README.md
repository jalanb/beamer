# Beamer

This small app provides a small app for BrightBeam

The app is iplemented as a single sccript, to be run like
```
$ python -m beamer
```

The app will this be found in `beamer/__main__.py`
Any business logic needed will be stored in the package rooted at `beamer/beamer'

# Usage

## Run the app

To run the app

1. Get the source code by either

     1.1 Unzip the code from `beamer.zip'
     1.2 Clone the repo from https://github.com/jalanb/beamer

If you are reading this then you have already found the code

2. Install the code

```
$ python -m pip install -e .
```

3. Run the code, e.g. 

```
$ python -m beamer
```

## Develop the code

A `pyproject.toml` file is provided whihc provides the a number of environments to aid development.
To use these fully you should first install `tox`, and then the project, e.g.

```
$ python -m pip install -e .[develop]
```

Note that there are a number of "levels" for installation, which bring in additional dependencies.:

1. The base project ("-e ."), has no extra ddependencies.
2. for testing ("-e .[test]"), brings in `tox`, `pytest`, and `coverage`
3. for linting ("-e .[lint]"), brings in `black`, `isort`, `flake8` and `mypy`.
4. for devops ("-e .[devops]") brings in'bump2version', 'build'.
5. for development ("-e .[develop]") brings in all of the above
6. for debugging tests ("-e .[pudb]") same as for development, buts adds `pudb`

The `pyproject.toml` is just my standard base project spec, and may need to be adjusted for this project as it expands.
