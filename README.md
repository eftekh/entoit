# entoit
LLM chatbot using LangChain for English to Italian translation. Full-stack web app in
FastAPI and TypeScript.

## Prerequisites

Python 3.10, Node.js 18, npm >= 9.5

## Development Tools

* Running the `install.sh` shell script will create a Python virtual environment
called `entoit` and install dev and project dependencies. To activate the `entoit`
venv, run:

    ```shell
    source .entoit/bin/activate
    ```

* The [`ci` module](ci/) provides a Python CLI tool for handling day-to-day development
tasks, including code linting and formatting, running unit tests, and other development
and deployment tasks. Usage instructions and the full list of available `ci` commands
can be found in the `ci` module [README](ci/README.md).
