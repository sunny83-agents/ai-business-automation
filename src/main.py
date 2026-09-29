from services.automation_service import (
    create_automation_task,
    get_all_tasks,
    update_task_status,
)

from workflow.automation_workflow import prepare_workflow
from services.execution_service import execute_workflow


def create_task():
    customer = input("Customer name: ")
    task = input("Automation task: ")

    try:
        result = create_automation_task(customer, task)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    print("\nAutomation task created:")
    print(f"ID: {result['id']}")
    print(f"Customer: {result['customer']}")
    print(f"Task: {result['task']}")
    print(f"Status: {result['status']}")


def list_tasks():
    tasks = get_all_tasks()

    if not tasks:
        print("\nNo automation tasks found.")
        return

    print("\nAutomation tasks:")

    for task in tasks:
        print(f"\nID: {task['id']}")
        print(f"Customer: {task['customer']}")
        print(f"Task: {task['task']}")
        print(f"Status: {task['status']}")
        print(f"Created: {task['created_at']}")


def change_task_status():
    task_id = input("Task ID: ")
    new_status = input("New status (ready/in_progress/completed): ")

    try:
        result = update_task_status(task_id, new_status)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    print("\nTask status updated:")
    print(f"ID: {result['id']}")
    print(f"Customer: {result['customer']}")
    print(f"Status: {result['status']}")


def run_workflow():
    tasks = get_all_tasks()

    if not tasks:
        print("\nNo automation tasks found.")
        return

    task = tasks[-1]

    try:
        workflow = prepare_workflow(task)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    print("\nAI Workflow prepared:")
    print(f"Task ID: {workflow['task_id']}")
    print(f"Customer: {workflow['customer']}")
    print(f"Action: {workflow['action']}")
    print(f"Status: {workflow['status']}")

    print("\nAI Plan:")
    for number, step in enumerate(workflow["steps"], start=1):
        print(f"{number}. {step}")

    print(f"\nExpected outcome: {workflow['expected_outcome']}")


def execute_latest_workflow():
    tasks = get_all_tasks()

    if not tasks:
        print("\nNo automation tasks found.")
        return

    task = tasks[-1]

    try:
        workflow = prepare_workflow(task)
        result = execute_workflow(workflow)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    print("\nWorkflow executed successfully:")
    print(f"Task ID: {result['task_id']}")
    print(f"Customer: {result['customer']}")
    print(f"Status: {result['status']}")

    print("\nCompleted steps:")
    for number, step in enumerate(result["completed_steps"], start=1):
        print(f"{number}. {step['step']}")

    print(f"\nResult: {result['result']}")
    print(f"Executed at: {result['executed_at']}")


def main():
    print("\nAI Business Automation")
    print("1. Create task")
    print("2. List tasks")
    print("3. Update task status")
    print("4. Prepare AI workflow")
    print("5. Execute latest workflow")

    choice = input("\nChoose an option: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        change_task_status()
    elif choice == "4":
        run_workflow()
    elif choice == "5":
        execute_latest_workflow()
    else:
        print("\nInvalid option.")


if __name__ == "__main__":
    main()