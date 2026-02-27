import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['title']} [{status}]")


def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")


def mark_completed(tasks):
    display_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark complete: "))
        tasks[choice - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid choice.")


def delete_task(tasks):
    display_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        tasks.pop(choice - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except (IndexError, ValueError):
        print("Invalid choice.")


def main():
    tasks = load_tasks()

    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()