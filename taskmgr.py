#!/usr/bin/env python3
"""
Task Manager CLI

Provides `add`, `list`, and `delete` commands to manage a
simple task list stored in the user's home directory.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import List


TASKS_DIR = Path.home() / ".taskmgr"
TASKS_FILE = TASKS_DIR / "tasks.json"


def load_tasks() -> List[dict]:
    """
    Load tasks from the tasks file.

    Returns:
    A list of task dictionaries. Each task has keys `id` and `name`.
    """
    if not TASKS_FILE.exists():
        return []
    try:
        with TASKS_FILE.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return []


def save_tasks(tasks: List[dict]) -> None:
    """
    Persist tasks to disk, creating the data directory if needed.

    Parameters:
    tasks (List[dict]): List of task dictionaries to save.
    """
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    with TASKS_FILE.open("w", encoding="utf-8") as fh:
        json.dump(tasks, fh, indent=2, ensure_ascii=False)


def add_task(name: str) -> dict:
    """
    Add a task with the provided name.

    Parameters:
    name (str): The task description.

    Returns:
    The created task dictionary.
    """
    tasks = load_tasks()
    next_id = 1 + max((t.get("id", 0) for t in tasks), default=0)
    task = {"id": next_id, "name": name}
    tasks.append(task)
    save_tasks(tasks)
    return task


def list_tasks() -> List[dict]:
    """
    Return the list of tasks.

    Returns:
    A list of task dictionaries.
    """
    return load_tasks()


def delete_task(task_id: int) -> bool:
    """
    Delete a task by its integer id.

    Parameters:
    task_id (int): The id of the task to delete.

    Returns:
    True if a task was deleted, False otherwise.
    """
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t.get("id") != task_id]
    if len(new_tasks) == len(tasks):
        return False
    save_tasks(new_tasks)
    return True


def main(argv: List[str] | None = None) -> int:
    """
    CLI entrypoint. Parses arguments and dispatches subcommands.

    Parameters:
    argv (List[str] | None): List of arguments or None to use sys.argv.

    Returns:
    Exit status code.
    """
    parser = argparse.ArgumentParser(prog="taskmgr")
    sub = parser.add_subparsers(dest="cmd")

    parser_add = sub.add_parser("add", help="Add a new task")
    parser_add.add_argument("name", help="Task description")

    sub.add_parser("list", help="List tasks")

    parser_del = sub.add_parser("delete", help="Delete a task by id")
    parser_del.add_argument("id", type=int, help="Task id to delete")

    args = parser.parse_args(argv)
    if args.cmd == "add":
        task = add_task(args.name)
        print(f"Added task {task['id']}: {task['name']}")
        return 0
    if args.cmd == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
            return 0
        for t in tasks:
            print(f"{t['id']}: {t['name']}")
        return 0
    if args.cmd == "delete":
        ok = delete_task(args.id)
        if ok:
            print(f"Deleted task {args.id}")
            return 0
        print(f"No task with id {args.id}")
        return 2

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

