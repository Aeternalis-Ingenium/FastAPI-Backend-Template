<h1 align=center><strong>DAPSQL FAR Project Template</strong></h1>

This is a template repository aimed to kick start your project with a setup from a real-world application! Now, let's disect the weird abbreviation from this repository title **DAQSQL FARN** which stands for:

* 🐳 [Dockerized](https://www.docker.com/)
* 🐘 [Asynchronous PostgreSQL](https://www.postgresql.org/docs/current/libpq-async.html)
* 🐍 [FastAPI](https://fastapi.tiangolo.com/)
* 🧬 [ReactJS](https://reactjs.org/)
* 💻 [TypeScript](https://www.typescriptlang.org/)

When the `Docker` is started, these are the URL addresses:

* Backend Application (API docs) $\rightarrow$ http://localhost:8001/docs
* Frontend Application $\rightarrow$ http://localhost:3001
* Database editor (Adminer) $\rightarrow$ http//lcoalhost:8081

## Why FARN-Stack?

Well, the easy anser is **Asynchronousity** and **Speed**!

* **FastAPI** is crowned as the fastest web framework for Python and thus we use it for our backend development.
* Meanwhile, **React** is a Java Script web framework that is easy to handle and offers lots of libraries from its community.
* The database of my choice is the **asynchronous** version of **PostgreSQL** (via [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)). Why asynchronous? Well.. Speed! Read [this blog from Packt](https://subscription.packtpub.com/book/programming/9781838821135/6/ch06lvl1sec32/synchronous-asynchronous-and-threaded-execution) if you want to educate yourself further about the topic **Asynchronous, Synchronous, Concurrency,** and **Parallelism**.
* And **Docker** is the technology that will hold your team together because your app will live in a container where the gravity of your personal machine specs don't matter anymore!

## Other Technologies

The above listed technologies are just the main ones. There are other technologies utilized in this project template to ensure that your application is robust and provides the best-possible development environment for your team! These technologies are:

* [TOML](https://toml.io/en/) $\rightarrow$ The one-for-all configuration file. This makes it simpler to setup our project.
* [Pyenv](https://github.com/pyenv/pyenv) $\rightarrow$ The simplest way to manage our Python versions.
* [Pyenv-VirtualEnv](https://github.com/pyenv/pyenv-virtualenv) $\rightarrow$ The plugin for `Pyenv` to manage the virtual environment for our packages.
* [PNPM](https://pnpm.io/) $\rightarrow$ This is `NPM` + `Yarn` on steroid. The highly-enhanced version of `NPM` which is `JavaScript` framework manager like `Pyenv` for python.
* [Pre-Commit](https://pre-commit.com/) $\rightarrow$ Git hook scripts to identify issues and quality of your code before pushing it to GitHub. These hooks are implemented for the following linting pakcages:
  * [Black (Python)](https://black.readthedocs.io/en/stable/) $\rightarrow$ Manage your code style with auto formatting and parallel continuous integration runner for Python.
  * [Isort (Python)](https://pycqa.github.io/isort/) $\rightarrow$ Sort your `import` for clarity. Also for Python. 
  * [MyPy (Python)](https://mypy.readthedocs.io/en/stable/) $\rightarrow$ A static type checker for Python that helps you write a cleaner code.
  * [ESLint (JavaScript)](https://eslint.org/) $\rightarrow$ Analyze your code for JavaScript.
* [Pre-Commit CI](https://pre-commit.ci/) $\rightarrow$ Continuous integration for our Pre-Commit hook that fixes and updates our hook versions.
* [Prettier](https://prettier.io/) $\rightarrow$ Format your JavaScript code to be more **prettier** 😜.
* [Husky](https://typicode.github.io/husky/#/) $\rightarrow$ Lint your commit messages, run tests, and javascript code.
* [CodeCov](https://about.codecov.io/) $\rightarrow$ A platform that analyze the result of your automated tests.
* [PyTest](https://docs.pytest.org/en/7.2.x/) $\rightarrow$ The testing framework for Python code.
* [JEST](https://jestjs.io/) $\rightarrow$ The testing framework for JavaScript code.
* [DBDiagram](https://dbdiagram.io/home) $\rightarrow$ A platform that lets your design your database by writing SQL and converting it into ERD. This paltform provides a complete symbol for entity relationships (not like many other platforms!).
* [GitHub Actions](https://github.com/features/actions) $\rightarrow$ The platform to setup our CI/CD by GitHub.
* [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) $\rightarrow$ The go-to database interface library for Python. The 2.0 is the most recent update where it provides asynchronous setup.
* [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) $\rightarrow$ A file for distributing the responsibilities in our project to each team/team mate.

The choice for my project development worklow is usually the [Trund-Based Development](https://trunkbaseddevelopment.com/), hence the name `trunk` for the main branch repository instead of `master` or `main`.

## Using this Template

Not a beginner? Great, here is the step to setup this template repository:

1. Backend setup:
   The backend server runs on http://localhost:8000

    ```shell
    cd backend

    mdkir coverage

    pyenv virtualenv 3.11.0 any_venv_name
    pyenv local any_venv_name

    pip3 install -r requirements.txt

    # Test run your backend server
    uvicorn src.main:backend_app --reload

    # Testing
    pytest  # Might throw an error without docker becasue of the imports
    ```

2. Frontend setup:
    The frontend server runs on http://localhost:3000

    ```shell
    cd frontend

    mkdir coverage

    pnpm install

    # Test run your frontend server
    pnpm start

    # Lint with Prettier
    pnpm lint:check # check only
    pnpm lint:fix   # automatically auto fix the issue

    # Lint with ESLint
    pnpm fmt:check  # check only
    pnpm fmt:fix    # automatically fix the issue

    # Testing
    pnpm test:notestpass    # Pass with no tests
    pnpm test               # Fail without any test
    ```

3. `Pre-Commit` setup:
    ```shell
    # Make sure you are in the ROOT project directory
    pre-commit install
    pre-commit update
    ```

4. `.env` setup:
    If you are not used to VIM or Linux CLI, then ignore the `echo` command and do it manually. All the secret variables for this template is located in `.env.example`.

    If you want to have another names for the secret variables, don't forget to change them also in:

    * `backend/src/config/base.py`
    * `docker-compose.yaml`

    ```shell
    # Make sure you are in the ROOT project directory
    touch .env

    echo "SECRET_VARIABLE=SECRET_VARIABLE_VALUE" >> .env
    ```

5. `CODEOWNERS` setup:
    Go to `.github/` and open `CODEOWNERS` file. This file is to assign the code to specific team member so you can distribute the weights of the project clearly.

6. Docker setup:
   ```shell
    # Make sure you are in the ROOT project directory
    chmod +x backend/entrypoint.sh
    chmod +x frontend/entrypoint.sh

    docker-compose build
    docker-compose up

    # Everytime you write a new code, update your container with:
    docker-compose up -d --build
   ```

7. (IMPORTANT) Finishing setup:
   ```shell
    # Generate revision for the database auto-migrations
    docker exec backend_app alembic revision --autogenerate -m "YOUR MIGRATION TITLE"
    docker exec backend_app alembic upgrade head    # to register the database classes

    # For testing within Docker container
    docker exec backend_app pytest      # backend
    docker exec frontend_app pnpm test  # frontend
   ```

8. Delete these files:

    * `README.md`
    * `CONTAINER.md`
    * `CICD.md`
    * `backend/README.md`
    * `frontend/README.md`

After running the inishing setup, you can go to all the URL addresses, to make sure that the containers are all running error-free!

---

## Guide

I also wrote some compact guide of what has been set up in this template repository. Find it below, if you are interested:

* [Part I: Backend App](https://github.com/Aeternalis-Ingenium/DAPSQL-FART-Stack-Template/trunk/backend)
* [Part II: Frontend App](https://github.com/Aeternalis-Ingenium/DAPSQL-FART-Stack-Template/trunk/frontend)
* [Part III: Containerization](https://github.com/Aeternalis-Ingenium/DAPSQL-FART-Stack-Template/trunk/CONTAINER.md)
* [Part IV: CI/CD](https://github.com/Aeternalis-Ingenium/DAPSQL-FART-Stack-Template/trunk/CICD.md)

---
