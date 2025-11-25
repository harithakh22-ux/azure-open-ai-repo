#!/usr/bin/env python3
"""Command-line interface for task management.

Commands:
  add <description>    Add a new task
  list                 List tasks
  delete <id>          Delete a task by id
"""

import argparse
from tasks import TaskManager


def main() -> None:
    parser = argparse.ArgumentParser(prog="taskcli", description="Task CLI: add, list, delete tasks")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("description", nargs="+", help="Task description")

    sub.add_parser("list", help="List tasks")

    p_del = sub.add_parser("delete", help="Delete task by id")
    p_del.add_argument("id", type=int, help="Task id to delete")
    p_del.add_argument("-y", "--yes", action="store_true", help="Skip confirmation")

    args = parser.parse_args()
    mgr = TaskManager()

    if args.command == "add":
        desc = " ".join(args.description).strip()
        if not desc:
            print("Empty description; nothing added.")
            return
        task = mgr.add_task(desc)
        print(f"Added task [{task['id']}] {task['description']}")

    elif args.command == "list":
        tasks = mgr.list_tasks()
        if not tasks:
            print("No tasks.")
            return
        for t in tasks:
            print(f"[{t['id']}] {t['description']}")

    elif args.command == "delete":
        tid = args.id
        if not args.yes:
            confirm = input(f"Delete task {tid}? [y/N]: ").strip().lower()
            if confirm not in ("y", "yes"):
                print("Aborted.")
                return
        ok = mgr.delete_task(tid)
        if ok:
            print(f"Deleted task {tid}.")
        else:
            print(f"Task {tid} not found.")


if __name__ == "__main__":
    main()

