from data_store import load_tasks, save_tasks


def create_automation_task(customer, task):
    if not customer.strip():
        raise ValueError("Customer name cannot be empty.")

    if not task.strip():
        raise ValueError("Automation task cannot be empty.")

    tasks = load_tasks()

    new_task = {
        "customer": customer.strip(),
        "task": task.strip(),
        "status": "ready"
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task