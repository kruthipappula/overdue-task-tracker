from datetime import datetime
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    name = input("Task name: ").strip()
    deadline = input("Deadline (MM-DD-YYYY): ").strip()

    try:
        datetime.strptime(deadline, "%m-%d-%Y")
    except ValueError:
        print("Invalid date format! Use MM-DD-YYYY.\n")
        return

    task = {"name": name, "deadline": deadline}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{name}' added!\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available!\n")
        return

    today = datetime.today()

    for i, task in enumerate(tasks, start=1):
        try:
            deadline_date = datetime.strptime(task['deadline'], "%m-%d-%Y")
        except ValueError:
           
            continue
        days_left = (deadline_date - today).days

        if days_left < 0:
            status = "🟥 OVERDUE"
        elif days_left <= 3:
            status = "🟨 Due Soon"
        else:
            status = "🟩 Active"

        print(f"{i}. {task['name']} — {task['deadline']} — {status}")
    print()

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete!\n")
        return

    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} — {task['deadline']}")

    try:
        choice = int(input("Enter the task number to delete: ").strip())
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['name']}\n")
        else:
            print("Invalid task number\n")
    except ValueError:
        print("Please enter a valid number\n")

def main():

    tasks = load_tasks()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
