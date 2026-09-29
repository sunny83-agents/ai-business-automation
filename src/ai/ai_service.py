def generate_automation_plan(task):
    if not task:
        raise ValueError("Task cannot be empty.")

    customer = task["customer"]
    action = task["task"].strip()

    if not customer.strip():
        raise ValueError("Customer name cannot be empty.")

    if not action:
        raise ValueError("Automation task cannot be empty.")

    steps = [
        f"Review the business request: {action}",
        "Identify the information and resources required",
        "Prepare the appropriate automation action",
        "Record the result of the automation",
    ]

    return {
        "customer": customer,
        "goal": action,
        "steps": steps,
        "expected_outcome": "The requested business automation is prepared for execution.",
        "status": "planned",
    }