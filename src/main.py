def create_automation_task(customer, task):
    return {
        "customer": customer,
        "task": task,
        "status": "ready"
    }


if __name__ == "__main__":
    customer = input("Customer name: ")
    task = input("Automation task: ")

    result = create_automation_task(customer, task)

    print("\nAutomation task created:")
    print(f"Customer: {result['customer']}")
    print(f"Task: {result['task']}")
    print(f"Status: {result['status']}")