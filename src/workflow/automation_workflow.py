def prepare_workflow(task):
    if not task:
        raise ValueError("Task cannot be empty.")

    return {
        "task_id": task["id"],
        "customer": task["customer"],
        "action": task["task"],
        "status": "ready"
    }