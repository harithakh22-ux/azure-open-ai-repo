# AGENTS.md - Coding Guidelines for Task Manager CLI

This file provides the coding guidelines Codex will follow 
when generating or refactoring code for the **Task Manager CLI** app.

## 1. Python Version
- **Use Python 3.12**: All code must be compatible with Python 3.12. 
Do not use deprecated features from older versions.

## 2. Code Style
- **Follow PEP8 conventions**:
  - Use **4 spaces** for indentation.
  - **Limit lines to 79 characters**.
  - Use **snake_case** for function and variable names (e.g., `add_task`, `list_tasks`).
  - **Import order**: Standard libraries first, third-party libraries second, and local imports last.

## 3. Docstrings
- **Add docstrings to all public functions**:
  - Every function must include a docstring explaining:
    - What the function does.
    - The function's parameters.
    - What the function returns.

  Example:
  ```python
  def add_task(task_name: str) -> None:
      """
      Adds a task to the task list.
      
      Parameters:
      task_name (str): The name of the task to be added.
      """
      pass

