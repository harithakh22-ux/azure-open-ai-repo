"""Simple task storage using a JSON file.

Provides a TaskManager class with `add_task`, `list_tasks`, and `delete_task`.
"""

from typing import List, Dict, Optional
import json
import os


DEFAULT_DB = os.path.join(os.path.dirname(__file__), "tasks.json")


class TaskManager:
    def __init__(self, path: Optional[str] = None):
        self.path = path or DEFAULT_DB
        self._ensure_db()

    def _ensure_db(self) -> None:
        if not os.path.exists(self.path):
            self._save([])

    def _load(self) -> List[Dict]:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save(self, tasks: List[Dict]) -> None:
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
        os.replace(tmp, self.path)

    def list_tasks(self) -> List[Dict]:
        """Return the list of tasks.

        Each task is a dict with `id` (int) and `description` (str).
        """
        return self._load()

    def add_task(self, description: str) -> Dict:
        """Add a new task with `description` and return the task dict."""
        tasks = self._load()
        next_id = max((t.get("id", 0) for t in tasks), default=0) + 1
        task = {"id": next_id, "description": description}
        tasks.append(task)
        self._save(tasks)
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by `task_id`.

        Returns True if a task was deleted, False if not found.
        """
        tasks = self._load()
        new_tasks = [t for t in tasks if t.get("id") != task_id]
        if len(new_tasks) == len(tasks):
            return False
        self._save(new_tasks)
        return True


__all__ = ["TaskManager"]

