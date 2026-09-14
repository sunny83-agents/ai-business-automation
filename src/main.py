from services.automation_service import create_automation_task


def main():
    customer = input("Customer name: ")
    task = input("Automation task: ")

    try:
        result = create_automation_task(customer, task)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    print("\nAutomation task created:")
    print(f"Customer: {result['customer']}")
    print(f"Task: {result['task']}")
    print(f"Status: {result['status']}")


if __name__ == "__main__":
    main()