# Welcome to Modular API

Modular API is a framework based on [FastAPI](https://fastapi.tiangolo.com/){target=_blank}, [Gino](https://python-gino.org/docs/en/master/index.html){target=_blank} and [alembic](https://alembic.sqlalchemy.org/en/latest/){target=_blank}.

## Advantages
- ### Based on [FastAPI](https://fastapi.tiangolo.com/){target=_blank}
    - All key features are availables out of box.

- ### Based on [Gino](https://python-gino.org/docs/en/master/index.html){target=_blank} too
    - All key features are availables out of box.
    - Provide an interface to use PostGreSQL databases.

- ### Integrate [Alembic](https://alembic.sqlalchemy.org/en/latest/){target=_blank} in our own command line interface
    - All key features are availables out of box.
    - autodetect database schema inside modules.
    - Raise an error if the database is not synchronized with the Gino schema at the application's startup.

- ### A great Command Line Interface
    - Upgrade your database schema from modules's db schemas.
    - Add modules from github or any git remote.
    - Create a new projet with an included virtual environnment in 1 command !

## Disadvantages

- ### Only available for PostgreSQL (for now)
Unfortunaly Gino is not yet compatible with Mysql but it's on the [Gino's roadmap](https://github.com/python-gino/gino/issues/381#issuecomment-629841406){target=_blank}