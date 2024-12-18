# Beamer

This small project provides a small app for BrightBeam

The app is iplemented as a single script, to be run like
```
$ python -m beamer
```

The script for the app will thus be found in `beamer/__main__.py`
Any business logic needed will be stored in the package rooted at `beamer/__init__.py`'

# Usage

## Run the app

To run the app

1. Get the source code by either

     1.1 Unzip the code from `beamer.zip`

     1.2 Clone the repo from https://github.com/jalanb/beamer

If you are reading this then you have already got the code

2. Install the code

Use `Python`'s normal `pip` module to install the code, e.g.
```
$ python -m pip install -e .
```

Note - it is often helpful to install the code in a virtual environment, e.g.

```
$ cd beamer
$ python -m venv --copies .venv
$ source .venv/bin/activate
$ python -m pip install -e .
```

## Run the app

Once installed you can run the code, e.g. 

```
$ python -m beamer
Price average among short trees: € 488,981.66
Price average among  tall trees: € 587,800.39
```

You may also specify files to be used for properties or trees, e.g.

```
$ python -m beamer --properties ../data/dublin-property.csv --trees ../data/dublin-trees.json
Price average among short trees: € 488,981.66
Price average among  tall trees: € 587,800.39
```

If you do not give paths to properties/trees files, then the app will use those already present in the root directory of the project.

## Develop the code

A basic `pyproject.toml` file is in the project, and provides a number of environments to aid development, e.g.

```
$ cd beamer
$ python -m pip install -e '.[develop]'
```

Note that there are a number of "levels" for installation, which bring in additional dependencies.:

1. The base project (`-e .`) has no extra dependencies.
2. for testing (`-e '.[test]'`) brings in `tox`, `pytest`, and `coverage`
3. for linting (`-e '.[lint]'`) brings in `black`, `isort`, `flake8` and `mypy`.
4. for devops (`-e '.[devops]'`) brings in `bump2version`, `build`.
5. for development (`-e '.[develop]'`) brings in all of the above, plus `ipython`, `pudb`, `sh` and better outputs from `pytest`.
6. for debugging tests (`-e '.[pudb]'`): same as for development, buts adds `pytest-pudb`

The `pyproject.toml` is just my standard base project spec, and may need to be adjusted for this project as it expands.

## Testing the code

The sources include a number of `doctest`s and `unittest`s

`doctest`s are simple tests, usually only "the happy path" tests. They are included primarily as documentation - quick examples of how to call functions, etc.

`unittest`s are more comprehensive, they will include more variations, and should cover most anticipated edge cases.

### Tox

Similarly to the "levels" of dependencies there are also "tox" environments specified in the `pyproject.toml`

These will allow using `tox` in different scenarios:

#### Linting

To run `black`, `blackdoc`, `flake8` and `mypy` tests:
```
$ tox -e lints
```

#### Testing

To run all `doctest`s and `unittest`s. 

Note that `tox` hands off the actual running of tests to `pytest`.
```
$ tox -e tests
```

After running tests `coverage` data is stored in a `.coverage` directory, allow you to view lines covered by tests in a standard way, e.g.
```
$ coverage html
$ open htmlcov/index.html
```

To run all tests "quick and dirty" use:
```
$ tox -e devs
```
This will 

1. stop after the first failure
2. not run any tests marked as "slow"
3. Ensure that all the tests are run in random order (which is not guaranteed with `$ tox -e tests`)

To allow debugging of `unittest`s:
```
$ tox -e pudb
```

This will open the `pudb` debugger on failing tests. 
