from services.automation_service import (
    create_automation_task,
    get_all_tasks,
)


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
    print(f"Created: {result['created_at']}")


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


def main():
    print("\nAI Business Automation")
    print("1. Create task")
    print("2. List tasks")

    choice = input("\nChoose an option: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        list_tasks()
    else:
        print("\nInvalid option.")


if __name__ == "__main__":
    main()