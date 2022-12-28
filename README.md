<h1 align=center><strong>FastAPI Backend Application Template</strong></h1>


This is a template repository aimed to kick start your project with a setup from a real-world application! This template utilizes the following tech-stack:

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

The above listed technologies are just the main ones. There are other technologies utilized in this project template to ensure that your application is robust and provides the best-possible development environment for your team! These technologies are:

* [TOML](https://toml.io/en/) $\rightarrow$ The one-for-all configuration file. This makes it simpler to setup our project.
* [Pyenv](https://github.com/pyenv/pyenv) $\rightarrow$ The simplest way to manage our Python versions.
* [Pyenv-VirtualEnv](https://github.com/pyenv/pyenv-virtualenv) $\rightarrow$ The plugin for `Pyenv` to manage the virtual environment for our packages.
* [Pre-Commit](https://pre-commit.com/) $\rightarrow$ Git hook scripts to identify issues and quality of your code before pushing it to GitHub. These hooks are implemented for the following linting pakcages:
  * [Black (Python)](https://black.readthedocs.io/en/stable/) $\rightarrow$ Manage your code style with auto formatting and parallel continuous integration runner for Python.
  * [Isort (Python)](https://pycqa.github.io/isort/) $\rightarrow$ Sort your `import` for clarity. Also for Python. 
  * [MyPy (Python)](https://mypy.readthedocs.io/en/stable/) $\rightarrow$ A static type checker for Python that helps you write a cleaner code.
* [Pre-Commit CI](https://pre-commit.ci/) $\rightarrow$ Continuous integration for our Pre-Commit hook that fixes and updates our hook versions.
* [CodeCov](https://about.codecov.io/) $\rightarrow$ A platform that analyze the result of your automated tests.
* [PyTest](https://docs.pytest.org/en/7.2.x/) $\rightarrow$ The testing framework for Python code.
* [DBDiagram](https://dbdiagram.io/home) $\rightarrow$ A platform that lets your design your database by writing SQL and converting it into ERD. This paltform provides a complete symbol for entity relationships (not like many other platforms!).
* [GitHub Actions](https://github.com/features/actions) $\rightarrow$ The platform to setup our CI/CD by GitHub.
* [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) $\rightarrow$ The go-to database interface library for Python. The 2.0 is the most recent update where it provides asynchronous setup.
* [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) $\rightarrow$ A file for distributing the responsibilities in our project to each team/team mate.

My choice for a project development worklow is usually the [Trunk-Based Development](https://trunkbaseddevelopment.com/) because of the straight forward approach in the collaboration workflow, hence the name `trunk` for the main branch repository instead of `master` or `main`.

## Setup Guide

This backend application is setup with `Docker`. Nevertheless, to understand how FastAPI works, read the [backend/README.md](https://github.com/Aeternalis-Ingenium/FastAPI-Backend-Template/trunk/backend/README.md).

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
    pre-commit update
    ```

5. Backend app credentials setup:
    If you are not used to VIM or Linux CLI, then ignore the `echo` command and do it manually. All the secret variables for this template is located in `.env.example`.

    If you want to have another names for the secret variables, don't forget to change them also in:

    * `backend/src/config/base.py`
    * `docker-compose.yaml`

    ```shell
    # Make sure you are in the ROOT project directory
    touch .env

    echo "SECRET_VARIABLE=SECRET_VARIABLE_VALUE" >> .env
    ```

6. `CODEOWNERS` setup:
    Go to `.github/` and open `CODEOWNERS` file. This file is to assign the code to specific team member so you can distribute the weights of the project clearly.

7. Docker setup:
   ```shell
    # Make sure you are in the ROOT project directory
    chmod +x backend/entrypoint.sh

    docker-compose build
    docker-compose up

    # Everytime you write a new code, update your container with:
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

## Local Setup

Read morea bout how the `backend/` application is set up [here](https://github.com/Aeternalis-Ingenium/FastAPI-Backend-Template/trunk/backend)

## Final Step

You can delete these 3 files (or change its content based on your need):
- `LICENSE.md`
- `README.md`
- `backend/README.md`

Enjoy your development and may your technology be forever useful to everyone 😉🚀🧬

---
