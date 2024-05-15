# The `ci` module

The `ci` module offers a Python CLI tool for handling day-to-day development tasks,
including setting up a development environment, applying code linting and formatting,
and other development and deployment tasks. 

The `ci` module defines functions that can be called as CLI commands from inside the
Python development environment `entoit` (see
[Development Tools](../README.md#Development-Tools)).

## Apply code formatting

```
python -m ci format
```

## Apply code linting

```
python -m ci lint
```

## Generate `requirements.txt` from `pyproject.toml`

```
python -m ci update-requirements
```

## Start the FastAPI backend server

```
python -m ci backend
```