<h1 align=center><strong>Part III: Containerization</strong></h1>

I setup the container with `docker-compose` because it is straight forward and provides 1 control file for all modules/apps that needs to be containerized. Our container names:

1. Database with Postgres Server: `db`
2. Adminer (Database Editor): `db_editor`
3. Backend Application: `backend_app`
4. Frontend APplication: `frontend_app`

## Dockerfile

There are 2 `Dockerfile`, 1 for each `backend` and 1 for `frontend`. The `Dockerfile` is where we design our application inside the Docker virtual machine. For example for `backend`, I

* install the latest `Python`,
* create venv,
* copy files from the actual directory, paste it into the virtual machine with this path `usr/backend`,
* Install the packages in my `requirements.txt`,
* Give the virtual machine the premission to be edited by me via the command `chmod +x`, and lastly
* run the backend server with `uvicorn`.

For the `frontend`, it is exactly the same procedure, but with commands for Node/React.

## Entrypoint.sh

This is `bash` script to make the containers start some processes over and over again, even if their requirement fails. For example, the `backend_app` needs `db` to be able to start... But.. Sometimes, the `backend_app` starts before the `db` starts, thus results in erro without my `entrypoint.sh` that let the `backend_db` restarts after 1 second.

## Docker-Compose

The `docker-compose.yaml` file is te control room of our `Docker` ship. It is where we

* define our containers (see list above!),
* register our secret environment variables,
* download images from postgres and adminer.

## Commands

When running these commands, the `Docker` dashboard needs to be running!

* Building our app in Docker virtual container:
  ```shell
  docker-compose build
  ```

* Start our app from within the container:
  ```shell
  docker-compose up
  ```

* Rebuil after we write new codes:
  ```shell
  docker-compose up -d --build
  ```

---
