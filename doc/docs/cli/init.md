---
title: init
description: init related command
---

```shell
ModularAPI init <my-project>
```
This command create a new project, init alembic migrations and venv.

???+ example
    ```
    ModularAPI init my-project
    ```
    ```
    INFO Initializing a new project at `my-project` ...
    INFO Creating the venv ...
    INFO Installing dependancies in the venv ...
    Collecting pip
    [...]
    SUCCESS You can now do `cd my-project` and start using ModularAPI

    WARNING Don't forget to edit `my-project\.env` !
    SUCCESS Done in 49.391s.
    ```
