# entoit
LLM chatbot for English to Italian translation, in FastAPI + TypeScript

## Development Tools

* Prerequisites: Python 3.10, Node.js 18, npm >= 9.5

* To set up the Python development environment,

    1. Create a Python virtual environment called `.entoit` using:

        ```
        python3 -m venv --upgrade-deps --clear --prompt entoit .entoit
        ```

        This command will replace any existing `.entoit` virtual environment.

    2. Activate the `.entoit` environment by running

        ```shell
        source .entoit/bin/activate
        ```

### The `ci` module

The `ci` module offers a Python CLI tool for handling day-to-day development tasks,
including setting up a development environment, applying code linting and formatting,
and other development and deployment tasks. To install the dependencies for the `ci`
module, run:

    ```
    python -m pip install -r ci/requirements.txt
    ```

The `ci` module defines functions that can be called as CLI commands. For instance,
to apply code formatting, run:

    ```
    python -m ci format
    ```
