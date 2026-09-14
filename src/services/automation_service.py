from datetime import datetime, timezone
from uuid import uuid4

from data_store import load_tasks, save_tasks

def create_automation_task(customer, task):
    if not customer.strip():
        raise ValueError("Customer name cannot be empty.")

    if not task.strip():
        raise ValueError("Automation task cannot be empty.")

    tasks = load_tasks()

    new_task = {
        "id": str(uuid4()),
        "customer": customer.strip(),
        "task": task.strip(),
        "status": "ready",
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task

def get_all_tasks():
    return load_tasks()

def update_task_status(task_id, new_status):
    allowed_statuses = {"ready", "in_progress", "completed"}

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid status. Choose one of: {', '.join(sorted(allowed_statuses))}"
        )

    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            save_tasks(tasks)
            return task

    raise ValueError(f"Task not found: {task_id}")