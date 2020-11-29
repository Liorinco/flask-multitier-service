# Flask multitier service

This project provides a Flask web service using multitier architecture.

## Installation

### Prerequisites

- Python 3.8
- `pipenv` (see https://realpython.com/pipenv-guide/#pipenv-introduction)

### Virtual environment installation

Use `pipenv`: https://realpython.com/pipenv-guide

To install the virtual environment:

```bash
pipenv install --dev
```

To load the virtual environment:

```bash
pipenv shell
```

### Development environment variables

Here the required environment variables for development purposes:
    - `DATABASE_NAME`: Name of the database to create
    - `DATABASE_USER`: User login to access the database
    - `DATABASE_PASSWORD`: User password to access the database

Note:
    `.env` file, located at repository root, allows to automatically set these environment variables when you enter the environment with `pipenv shell` command.

### Local infrastructure installation

Use `docker-compose`: https://docs.docker.com/compose/
Components:
    - PostgreSQL database

To run the infrastructure:

```bash
docker-compose up --detach
```

To turn off the infrastructure:

```bash
docker-compose down
```

To destroy the infrastructure:

```bash
docker-compose down --volumes
```

## Usage

### Run the service

```bash
python -m service
```

### Run tests

Use `pytest`: https://docs.pytest.org/en/stable/usage.html

To run all the tests:

```bash
pytest
```
