# The `ci` module

The `ci` module offers a Python CLI tool for handling day-to-day development tasks,
including setting up a development environment, applying code linting and formatting,
and other development and deployment tasks. 

Running the `ci/install.sh` shell script will create a Python virtual environment
called `entoit` and install `ci` and project dependencies. To activate the `entoit`
venv, run:

    ```shell
    source .entoit/bin/activate
    ```

The `ci` module defines functions that can be called as CLI commands from inside
`entoit`.

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