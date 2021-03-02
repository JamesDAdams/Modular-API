---
title: Modules
description: Modules related commands
---


# Modules

Modules command can be call by using the following command :
```shell
ModularAPI modules
```

!!! warning
    You must be at the top of your project's hierarchy to use this command (`/path/example/myproject/`)


## Add a module

```shell
ModularAPI modules add <GitRemoteUrl>
```
Add a module from a git remote to `./modules` folder.

???+ example

    ```
    ModularAPI modules add https://github.com/Joffref/The-ToolBox-
    ```

??? info
    Under the hood it performs a git clone.


## Update module

```shell
ModularAPI modules update <ModuleName>
```
Update a module in current `./modules` folder from its git remote.

???+ example

    ```
    ModularAPI modules update ModuleA
    ```

??? warning
    If the git remote is unvailable it will raise an error.

## Update all modules

```shell
ModularAPI modules update all
```
Udate all modules in `./modules` folder with a git remote configured.

!!! danger
    Don't name your module all.

## Remove module

```shell
ModularAPI modules remove <ModuleName>
```
Remove a module from current `./modules` folder.





## Remove all modules

```shell
ModularAPI modules remove all
```
Remove all modules from current `./modules` folder.

!!! danger
    Don't name your module all.


## List all installed modules
```shell
ModularAPI modules list
```
List all modules from current `./modules` folder.

