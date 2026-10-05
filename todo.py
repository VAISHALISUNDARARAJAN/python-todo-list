tasks = []


def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    title = input("Enter task: ").strip()

    if title == "":
        print("Task cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")

    for i, task in enumerate(tasks, 1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{i}. {task['title']} - {status}")


def complete_task():
    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter the task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        if tasks[number - 1]["completed"]:
            print("Task is already completed.")
        else:
            tasks[number - 1]["completed"] = True
            print("Task completed successfully!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter the task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        deleted_task = tasks.pop(number - 1)

        print(f"Task '{deleted_task['title']}' deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")


while True:
    show_menu()

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
