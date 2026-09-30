# Overdue Task Tracker

A very basic, simple task tracker built with Python. The program allows users to add tasks with deadlines, view their current status, and delete tasks.

## Features

- Add tasks with given deadline
- Enter dates using the `MM-DD-YYYY` format
- View all saved tasks
- Identify task status:
  - 🟩 Active
  - 🟨 Due Soon
  - 🟥 Overdue
- Delete tasks by task number and by completion
- Store tasks in `tasks.json`

## Technologies Used

- Python
- JSON
- `datetime` module

## How to Run

Make sure Python 3 is installed, then run:

```bash
python tracker.py
```

## How to Use

When the program starts, choose an option from the menu:

```text
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
```

### Add a Task

Enter the task name and deadline.

```text
Task name: Submit assignment
Deadline (MM-DD-YYYY): 09-29-2026
```

### View Tasks

The program displays each task along with its deadline and status.

```text
1. Submit assignment — 10-15-2026 — 🟩 Active
```

### Delete a Task

Select the task number you want to remove.

## Files

```text
overdue-task-tracker/
├── tracker.py
├── tasks.json
└── README.md
```

The `tasks.json` file stores the task information and is updated whenever a task is added or deleted.

## Future Improvements
I will improve this project by adding the following features to make it more elaborate:
- Adding an option to edit tasks
- Sorting tasks by priority deadline
- Marking tasks as completed
- Adding an user interface
