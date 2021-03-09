## Description
The setting is the provided way to configure the application :

## Environment configuration
In order to easily manage differents types of configurations you can use env variable.

!!! info
    It is possible to configure multiple env using `.env` files.

??? example "Linux"
    ```
    DOTENV_PATH=dev.env venv/bin/uvicorn modularapi.asgi:app --reload
    ```
    ```
    DOTENV_PATH=prod.env venv/bin/gunicorn modularapi.asgi:app -k uvicorn.workers.UvicornWorker
    ```

???+ example "Windows TODO"
    ```
    TODO
    ```

### 