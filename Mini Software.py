tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\n--- Task List ---")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")


def add_task():
    task = input("\nEnter new task: ")
    tasks.append(task)
    print("Task added successfully!")


def edit_task():
    show_tasks()

    if len(tasks) > 0:
        number = int(input("\nEnter task number to edit: "))

        if 1 <= number <= len(tasks):
            new_task = input("Enter new task description: ")
            tasks[number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")


def delete_task():
    show_tasks()

    if len(tasks) > 0:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")


def menu():
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()

        elif choice == "2":
            add_task()

        elif choice == "3":
            edit_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Exiting Task Manager...")
            break

        else:
            print("Invalid choice. Try again.")


menu()