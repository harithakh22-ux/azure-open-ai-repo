Task Manager CLI
================

A tiny command line app to add, list, and delete tasks.

Usage
-----

- Add a task:

```sh
python taskmgr.py add "Buy milk"
```

- List tasks:

```sh
python taskmgr.py list
```

- Delete a task by id:

```sh
python taskmgr.py delete 2
```

Data storage
------------

Tasks are stored in `~/.taskmgr/tasks.json`.

