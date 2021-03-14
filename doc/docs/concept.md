ModularAPI is designed in 3 parts:

### The CLI
The **CLI** (**c**ommand **l**ine **i**nterface) is the tool you use to manage your modular projects and your databases migrations:<br>
With the CLI you can :

- Create a new project (see [cli/init](/cli/init/){target=_blank})
- upgrade the database schema (see [cli/db](/cli/db/){target=_blank})
- Manage modules:
    - [add](/cli/modules/#add-a-module){target=_blank}
    - [update](/cli/modules/#update-a-module){target=_blank}
    - [update](/cli/modules/#update-a-module){target=_blank}
    - [remove](/cli/modules/#remove-a-module){target=_blank}
    - ect ...

### The core
The core loads modules and ensure the coherence between the database and described schemas.

### Modules
modules are the main concept of the framework, a module is basically a folder with Python scripts :
```
my-project
│   .env
│   alembic.ini
│   requirements.txt
│
├───db_migrations
│   │   env.py
│   │   README
│   └───script.py.mako
│
├───modules
│   ├───module-a
│   │       db.py
│   │       main.py
│   │       requirements.txt
│   │
│   └───module-b
│           db.py
│           main.py
│           requirements.txt
│
└───venv
    ├─── [...]
```

The `main.py` is the entrypoint of the module, it have one hook :

#### module hooks

##### on_load function

The `on_load` hook is triggered at the startup of the app and take the app (an instance of FastAPI) as argument.
You can declare your API endpoint or call whatever code you want.
!!! warning
    the `on_load` hook is triggered before the database (gino engine) was initialized.<br />
    See the part about how to use coroutine as on_load bellow.


- **on_load**

!!! example
    ```py
    # coding: utf-8
    from pathlib import Path

    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles


    def on_load(app: FastAPI):
        @app.get("/api/users", tags=["users"])
        async def read_users():
            return [{"username": "Rick"}, {"username": "Morty"}]

        # serve a spa build (frontend)
        p = Path(__file__).parent / "dist"
        app.mount("/user", StaticFiles(directory=p, html=True), name="static")
    ```

- **on_load coroutine (async)**

`on_load` can also be a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutines){target=_blank}:
!!! example
    ```py
    async def on_load(app: FastAPI):
        import asyncio

        from modularapi.db import db
        from modularapi.settings import get_setting
        await db.set_bind(get_setting().PG_DNS) # connect to the database

        all_users: List[MyGinoModel] = await MyGinoModel.query.gino.all()
        await db.pop_bind().close() # close the connection
        print(all_users) # [<modules.my_module.db.MyModel object at 0x0000020F8B273310>, ...]
        await asyncio.sleep(10)
        print("done")
    ```

!!! info
    Under the hood it run `asyncio.run` in a new `thread` to ensure the `on_load` hook is finished before continue loading others modules or start the app

!!! tips
    According to the thing

!!! warning
    - Given that we have to use thread to correctly handle async on_load hook's end you must use a classic (not async) function if you want to use the Uvicorn/Gunicorn's event loop
    - For now possibles raised exceptions that could happen in the coroutine are not traced back to the main thread (but they are printed in stderr) !
