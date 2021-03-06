---
title: init
description: init related command
---

```shell
ModularAPI init <nom du projet>
```
This command create a new project, init alembic migrations and venv.

???+ example
    ```
    ModularAPI init project
    ```
    ```
    INFO Initializing a new projet at `project` ...
    INFO Creating the venv ...
    INFO Installing dependancies in the venv ...
    Collecting pip
    [...]
    SUCCESS You can now do `cd project` and start using ModularAPI

    WARNING Don't forget to edit `project\.env` !
    SUCCESS Done in 49.391s.
    ```
