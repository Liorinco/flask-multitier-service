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

### Required environment variables

Here the required environment variables to make the service available:
- `DATABASE_URI`:  
    URI to access the database.  
    Format: `{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}`  
    Example: `postgresql://db_user:db_password@localhost:5432/db_name`  

### Development environment variables

Here the required environment variables for development purposes:
- `DATABASE_NAME`: Name of the database to create
- `DATABASE_USER`: User login to access the database
- `DATABASE_PASSWORD`: User password to access the database

> Note:  
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

### Make the database up to date

Use `alembic`: https://alembic.sqlalchemy.org/en/latest/

To update the database executing migrations:

```bash
alembic upgrade head
```

To see the list of migrations:

```bash
alembic history
```

To rollback to a migration:

```bash
alembic downgrade {REVISION_ID}
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

## Development tools

### Create a new database migration

Use `alembic`: https://alembic.sqlalchemy.org/en/latest/

Here the procedure:
1. Create/update the concerned DAO from `service/infractructure/daos`
2. Générate the migration:
    ```bash
    alembic revision --autogenerate -m "Migration title"
    ```
