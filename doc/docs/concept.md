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

The `main.py` is the entrypoint of the module, it have some hook :

- `on_load(app: FastAPI)`
??? example
    ```py
    # coding: utf-8
    from pathlib import Path

    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles


    def load_module(app: FastAPI):
        @app.get("/api/users", tags=["users"])
        async def read_users():
            return [{"username": "Rick"}, {"username": "Morty"}]

        # serve a spa build (frontend)
        p = Path(__file__).parent / "dist"
        app.mount("/user", StaticFiles(directory=p, html=True), name="static")
    ```

- `on_build()`
??? example
    ```py
    # coding: utf-8

    from pathlib import Path

    def on_build():
        import subprocess

        p = Path(__file__).parent / "frontend"
        # build a nuxt js frontend
        subprocess.run(["yarn"], shell=True, cwd=p)
        subprocess.run(["yarn", "build"], shell=True, cwd=p)
    ```
