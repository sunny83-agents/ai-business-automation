def create_automation_task(customer, task):
    if not customer.strip():
        raise ValueError("Customer name cannot be empty.")

    if not task.strip():
        raise ValueError("Automation task cannot be empty.")

    return {
        "customer": customer.strip(),
        "task": task.strip(),
        "status": "ready"
    }