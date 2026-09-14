from ai.ai_service import generate_automation_plan


def prepare_workflow(task):
    if not task:
        raise ValueError("Task cannot be empty.")

    workflow = {
        "task_id": task["id"],
        "customer": task["customer"],
        "action": task["task"],
        "status": "ready"
    }

    workflow["ai_plan"] = generate_automation_plan(task)

    return workflow