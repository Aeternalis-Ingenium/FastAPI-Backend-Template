<h1 align=center><strong>FastAPI Backend Application Template</strong></h1>

<div align=center>
 <a href="https://github.com/Aeternalis-Ingenium/FastAPI-Backend-Template/actions/workflows/ci-backend.yaml">
  <img src="https://github.com/Aeternalis-Ingenium/FastAPI-Backend-Template/actions/workflows/ci-backend.yaml/badge.svg"/> 
 </a>

 <a href="https://codecov.io/gh/Aeternalis-Ingenium/FastAPI-Backend-Template">
  <img src="https://codecov.io/gh/Aeternalis-Ingenium/FastAPI-Backend-Template/branch/trunk/graph/badge.svg?token=1hiVayuLRl"/> 
 </a>

 <a href="https://github.com/pre-commit/pre-commit">
  <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit" alt="pre-commit" style="max-width:100%;">
 </a>

 <a href="https://github.com/psf/black">
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg">
 </a>

 <a href="https://pycqa.github.io/isort/">
  <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336">
 </a>

 <a href="http://www.mypy-lang.org/static/mypy_badge.svg">
  <img src="https://camo.githubusercontent.com/59eab954a267c6e9ff1d80e8055de43a0ad771f5e1f3779aef99d111f20bee40/687474703a2f2f7777772e6d7970792d6c616e672e6f72672f7374617469632f6d7970795f62616467652e737667" alt="check with mypy" style="max-width:100%;">
 </a>
</div>

<br>

This is a template repository aimed to kick-start your project with a setup from a real-world application! This template utilizes the following tech stack:

* 🐳 [Dockerized](https://www.docker.com/)
* 🐘 [Asynchronous PostgreSQL](https://www.postgresql.org/docs/current/libpq-async.html)
* 🐍 [FastAPI](https://fastapi.tiangolo.com/)

When the `Docker` is started, these are the URL addresses:

* Backend Application (API docs) $\rightarrow$ `http://localhost:8001/docs`
* Database editor (Adminer) $\rightarrow$ `http//localhost:8081`

The backend API without `Docker` can be found in `http://localhost:8000/docs`.

## Why the above Tech-Stack?

Well, the easy answer is **Asynchronousity** and **Speed**!

* **FastAPI** is crowned as the fastest web framework for Python and thus we use it for our backend development.
* The database of my choice is the **asynchronous** version of **PostgreSQL** (via [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)). Read [this blog from Packt](https://subscription.packtpub.com/book/programming/9781838821135/6/ch06lvl1sec32/synchronous-asynchronous-and-threaded-execution) if you want to educate yourself further about the topic **Asynchronous, Synchronous, Concurrency,** and **Parallelism**.
* **Docker** is a technology that packages an application into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime.

## Other Technologies

The above-listed technologies are just the main ones. There are other technologies utilized in this project template to ensure that your application is robust and provides the best possible development environment for your team! These technologies are:

* [TOML](https://toml.io/en/) $\rightarrow$ The one-for-all configuration file. This makes it simpler to setup our project.
* [Pyenv](https://github.com/pyenv/pyenv) $\rightarrow$ The simplest way to manage our Python versions.
* [Pyenv-VirtualEnv](https://github.com/pyenv/pyenv-virtualenv) $\rightarrow$ The plugin for `Pyenv` to manage the virtual environment for our packages.
* [Pre-Commit](https://pre-commit.com/) $\rightarrow$ Git hook scripts to identify issues and quality of your code before pushing it to GitHub. These hooks are implemented for the following linting packages:
  * [Black (Python)](https://black.readthedocs.io/en/stable/) $\rightarrow$ Manage your code style with auto-formatting and parallel continuous integration runner for Python.
  * [Isort (Python)](https://pycqa.github.io/isort/) $\rightarrow$ Sort your `import` for clarity. Also for Python. 
  * [MyPy (Python)](https://mypy.readthedocs.io/en/stable/) $\rightarrow$ A static type checker for Python that helps you to write cleaner code.
* [Pre-Commit CI](https://pre-commit.ci/) $\rightarrow$ Continuous integration for our Pre-Commit hook that fixes and updates our hook versions.
* [CodeCov](https://about.codecov.io/) $\rightarrow$ A platform that analyzes the result of your automated tests.
* [PyTest](https://docs.pytest.org/en/7.2.x/) $\rightarrow$ The testing framework for Python code.
* [DBDiagram](https://dbdiagram.io/home) $\rightarrow$ A platform that lets your design your database by writing SQL and converting it into ERD. This platform provides a complete symbol for entity relationships (not like many other platforms!).
* [GitHub Actions](https://github.com/features/actions) $\rightarrow$ The platform to setup our CI/CD by GitHub.
* [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) $\rightarrow$ The go-to database interface library for Python. The 2.0 is the most recent update where it provides an asynchronous setup.
* [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) $\rightarrow$ A file for distributing the responsibilities in our project to each team/teammate.

My choice for a project development workflow is usually the [Trunk-Based Development](https://trunkbaseddevelopment.com/) because of the straightforward approach in the collaboration workflow, hence the name `trunk` for the main branch repository instead of `master` or `main`.

## What Code is included?

For the backend application:
* The project, linter, and test configurations in `backend/pyproject.toml`.
* 3 settings classes (development, staging, production) with the super class in `backend/src/config/settings/base.py`.
* Event logger in `backend/src/config/events.py`.
* The `Account` object table model in `backend/src/models/db/account.py`.
* The `Account` object schema model in `backend/src/models/schemas/account.py`.
* PostgreSQL database connection with asynchronous SQLAlchemy 2.0 in `backend/src/repository/database.py`.
* A custom SQLAlchemy Base class in `backend/src/repository/table.py`
* PostgreSQL database connection with asynchronous SQLAlchemy 2.0 in `backend/src/repository/database.py`.
* Database-related events e.g. database table registration by app startup in `backend/src/repository/events.py`.
* C. R. U. D. methods for `Account` object in `backend/src/repository/crud/account.py`.
* Table classes registration file in `backend/src/repository/base.py`.
* Alembic setup for auto-generating asynchronous database migrations in `backend/src/repository/migration/**`.
* Alembic main configuration file in `backend/alembic.ini`.
* Dependency injection for database session and repository in `backend/src/api/**`.
* API endpoints for `Account` signup and signin in `backend/src/api/routes/authentication.py`.
* API endpoints for `Account` get all, get 1, update, and delete in `backend/src/api/routes/account.py`.
* API endpoints registration file in `backend/src/api/endpoints`.
* Hashing and JWT generators and simple verification functions in `backend/src/securities/**`.
* Helper functions, string messages, and error handling in `backend/src/utilities/**`.
* A comprehensive FastAPI application initialization in `backend/src/main.py`.

For testing, I have prepared the following simple code to kick-start your test-driven development:
* A simple replication of the backend application for testing purposes and the asynchronous test client in `backend/tests/conftest.py`.
* 2 simple test functions to test the backend application initialization in `tests/unit_tests/test_src.py`.

For the DevOps:
* A simple `build` job to test the compilation of the source code for the backend application in `.github/workflows/ci-backend.yaml`.
* A simple linting job called `code-style` with black, isort, flake8, and mypy in `.github/workflows/ci-backend.yaml`.
* An automated testing with `PyTest` and an automated test reporting with `Codecov` in in `.github/workflows/ci-backend.yaml`.
* A source code responsibility distribution file in `.github/CODEOWNERS` (Please change the username to your own).
* A `YAML` file for an automated semantic commit message in `.github/workflows/ci-backend.yaml`.
* An automated test report monitoring via `Codecov` in `codecov.yaml`
* A CI for automatically updating all linter version in the pre-commit `YAML` file in `.pre-commit-config.YAML`.

For containerization:
* A `Docker` configuration that utilizes the latest Python image in `backend/Dockerfile`.
* A script that ensure the backend application will restart when postgres image hasn't started yet in `backend/entrypoint.sh`.
* Setting up `Postgres` image for our database server, `Adminer` for our database editor, and `backend_app` for our backend application's container in `docker-compose.yaml`.

For the team development environment:
* A pre-commit hooks for `Black`, `Isort`, and `MyPy` to ensure the conventional commit message before pushing an updated code into the remote repository in `.pre-commit-config.YAML`.
* All secret variables are listed in `.env.example`. You need to copy these variables and set the values respectively to your need and save them in a new `.env` in the root directory.

## Setup Guide

This backend application is setup with `Docker`. Nevertheless, you can see the full local setup without `Docker` in [backend/README.md](https://github.com/Aeternalis-Ingenium/FastAPI-Backend-Template/blob/trunk/backend/README.md).

1. Before setting up the backend app, please create a new directory called `coverage` for the testing report purpose:
   ```shell
   cd backend && mkdir coverage
   ```

2. Backend app setup:
    ```shell
    # Creating VENV
    pyenv virtualenv 3.11.0 any_venv_name
    pyenv local any_venv_name

    # Install dependencies
    pip3 install -r requirements.txt

    # Test run your backend server
    uvicorn src.main:backend_app --reload
    ```

3. Testing with `PyTest`:
   Make sure that you are in the `backend/` directory.
   ```shell
   # For testing without Docker
   pytest
   
   # For testing within Docker
   docker exec backend_app pytest
   ```

4. `Pre-Commit` setup:
    ```shell
    # Make sure you are in the ROOT project directory
    pre-commit install
    pre-commit autoupdate
    ```

5. Backend app credentials setup:
    If you are not used to VIM or Linux CLI, then ignore the `echo` command and do it manually. All the secret variables for this template are located in `.env.example`.

    If you want to have another name for the secret variables, don't forget to change them also in:

    * `backend/src/config/base.py`
    * `docker-compose.yaml`

    ```shell
    # Make sure you are in the ROOT project directory
    touch .env

    echo "SECRET_VARIABLE=SECRET_VARIABLE_VALUE" >> .env
    ```

6. `CODEOWNERS` setup:
    Go to `.github/` and open `CODEOWNERS` file. This file is to assign the code to a specific team member so you can distribute the weights of the project clearly.

7. Docker setup:
   ```shell
    # Make sure you are in the ROOT project directory
    chmod +x backend/entrypoint.sh

    docker-compose build
    docker-compose up

    # Every time you write a new code, update your container with:
    docker-compose up -d --build
   ```

8. (IMPORTANT) Database setup:
   ```shell
    # (Docker) Generate revision for the database auto-migrations
    docker exec backend_app alembic revision --autogenerate -m "YOUR MIGRATION TITLE"
    docker exec backend_app alembic upgrade head    # to register the database classes
    
    # (Local) Generate revision for the database auto-migrations
    alembic revision --autogenerate -m "YOUR MIGRATION TITLE"
    alembic upgrade head    # to register the database classes
   ```

9. Go to https://about.codecov.io/, and sign up with your github to get the `CODECOV_TOKEN`

10. Go to your GitHub and register all the secret variables (look in .env.example) in your repository (`settings` $\rightarrow$ (scroll down a bit) `Secrets` $\rightarrow$ `Actions` $\rightarrow$ `New repository secret`)

**IMPORTANT**: Without the secrets registered in Codecov and GitHub, your `CI` will fail and life will be horrible 🤮🤬
**IMPORTANT**: Remember to always run the container update every once in a while. Without the arguments `-d --build`, your `Docker` dashboard will be full of junk containers!

## Project Structure

```shell
.github/
├── workflows/
    ├── ci-backend.yaml                 # A CI file for the backend app that consists of `build`, `code-style`, and `test`
├── CODEOWNERS                          # A configuration file to distribute code responsibility
├── semantic.yaml                       # A configuration file for ensuring an automated semantic commit message

backend/
├── coverage/
├── src/
    ├── api/
        ├── dependencies/               # Dependency injections
            ├── session.py
            ├──repository.py
        ├── routes/                     # Endpoints
            ├── account.py              # Account routes
            ├── authentication.py       # Signup and Signin routes
        ├── endpoints.py                # Endpoint registration
    ├── config/
        ├── settings/
            ├── base.py                 # Base settings / settings parent class
                ├── development.py      # Development settings
                ├── environments.py     # Enum with PROD, DEV, STAGE environment
                ├── production.py       # Production settings
                ├── staging.py          # Test settings
        ├── events.py                   # Registration of global events
        ├── manager.py                  # Manage get settings
    ├── models/
        ├── db/
            ├── account.py              # Account class for database entity
        ├── schemas/
            ├── account.py              # Account classes for data validation objects
            ├── base.py                 # Base class for data validation objects
    ├── repository/
        ├── crud/
            ├── account.py              # C. R. U. D. operations for Account entity
            ├── base.py                 # Base class for C. R. U. D. operations
        ├── migrations/
            ├── versions/
            ├── env.py                  # Generated via alembic for automigration
            ├── script.py.mako          # Generated via alembic
        ├── base.py                     # Entry point for alembic automigration
        ├── database.py                 # Database class with engine and session
        ├── events.py                   # Registration of database events
        ├── table.py                    # Custom SQLAlchemy Base class
    ├── security/
        ├── hashing/
            ├── hash.py                 # Hash functions with passlib
            ├── password.py             # Password generator with hash functions
        ├── authorizations/
            ├── jwt.py                  # Generate JWT tokens with python-jose
        ├── verifications/
            ├── credentials.py          # Check for attributes' availability
    ├── utilities/
        ├── exceptions/
            ├── http/
                ├── http_exc_400.py     # Custom 400 error handling functions
                ├── http_exc_401.py     # Custom 401 error handling functions
                ├── http_exc_403.py     # Custom 403 error handling functions
                ├── http_exc_404.py     # Custom 404 error handling functions
            ├── database.py             # Custom `Exception` class
            ├── password.py             # Custom `Exception` class
        ├── formatters/
            ├── datetime_formatter.py   # Reformat datetime into the ISO form
            ├── field_formatter.py      # Reformat snake_case to camelCase
        ├── messages/
            ├── http/
                ├── http_exc_details.py	# Custom message for HTTP exceptions
    ├── main.py                         # Our main backend server app
├── tests/
    ├── end_to_end_tests/               # End-to-end tests
    ├── integration_tests/              # Integration tests
    ├── security_tests/                 # Security-related tests
    ├── unit_tests/                     # Unit tests
        ├── test_src.py                 # Testing the src directory's version
    ├── conftest.py                     # The fixture codes and other base test codes
├── Dockerfile                          # Docker configuration file for backend application
├── README.md                           # Documentation for backend app
├── entrypoint.sh                       # A script to restart backend app container if postgres is not started
├── alembic.ini                         # Automatic database migration configuration
├── pyproject.toml                      # Linter and test main configuration file
├── requirements.txt                    # Packages installed for backend app
.dockerignore                           # A file that list files to be excluded in Docker container
.gitignore                              # A file that list files to be excluded in GitHub repository
.pre-commit-config.yaml                 # A file with Python linter hooks to ensure conventional commit when committing
LICENSE.md                              # A license to use this template repository (delete this file after using this repository)
README.md                               # The main documentation file for this template repository
codecov.yaml                            # The configuration file for automated testing CI with codecov.io
docker-compose.yaml                     # The main configuration file for setting up a multi-container Docker
```

## Final Step

You can delete these 3 files (or change its content based on your need):
- `LICENSE.md`
- `README.md`
- `backend/README.md`

Enjoy your development and may your technology be forever useful to everyone 😉🚀🧬

---
