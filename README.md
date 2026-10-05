# Python To-Do List Application

A simple command-line To-Do List application developed using Python.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Shows Pending and Completed status
- Saves tasks using JSON file persistence
- Loads saved tasks when the program starts
- Handles invalid menu choices
- Handles invalid task numbers
- Handles empty task input
- Uses Python lists, dictionaries and functions

## Technologies Used

- Python
- JSON

## How to Run

1. Make sure Python is installed on your computer.
2. Open `todo.py` using Python IDLE or any Python IDE.
3. Run the program.
4. Select an option from the menu.
5. Follow the instructions displayed on the screen.

## Available Operations

| Option | Operation |
|--------|-----------|
| 1 | Add Task |
| 2 | View Tasks |
| 3 | Complete Task |
| 4 | Delete Task |
| 5 | Exit |

## Data Persistence

Tasks are stored in a `tasks.json` file.

The application automatically:

- Saves tasks when a task is added.
- Saves changes when a task is completed.
- Saves changes when a task is deleted.
- Loads saved tasks when the application starts.

## Example

```text
===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Enter your choice (1-5): 1
Enter task: Study Python
Task added successfully!

Enter your choice (1-5): 2

Your Tasks:
1. Study Python - Pending

Enter your choice (1-5): 3
Enter the task number to complete: 1
Task completed successfully!

Your Tasks:
1. Study Python - Completed

Error Handling
The application handles:
Empty task input
Invalid menu choices
Invalid task numbers
Non-numeric input when a task number is required
Missing or invalid JSON file
Project Structure
python-todo-list/
│
├── todo.py
├── tasks.json
├── README.md
└── screenshots/
    ├── add-task.png
    ├── view-task.png
    ├── complete-task.png
    ├── delete-task.png
    └── .gitkeep
Demo Screenshots
The screenshots folder contains examples of adding, viewing, completing and deleting tasks.
