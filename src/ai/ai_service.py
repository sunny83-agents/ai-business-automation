def generate_automation_plan(task):
    if not task:
        raise ValueError("Task cannot be empty.")

    customer = task["customer"]
    action = task["task"]

    return {
        "customer": customer,
        "action": action,
        "plan": f"Prepare and execute the following automation: {action}",
        "status": "planned"
    }