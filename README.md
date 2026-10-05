# Python To-Do List Application

A simple command-line To-Do List application developed using Python.

## Features

- Add new tasks
- View all tasks
- Mark a particular task as completed
- Delete a particular task
- Shows Pending and Completed status
- Handles invalid menu choices
- Handles invalid task numbers
- Uses Python lists, dictionaries and functions

## Technologies Used

- Python

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

Enter your choice (1-5): 4
Enter the task number to delete: 1

Error Handling
The application handles:
Empty task input
Invalid menu choices
Invalid task numbers
Non-numeric input when a task number is required
Project Structure
python-todo-list/
│
├── todo.py
├── README.md
└── screenshots/
    ├── add-task.png
    ├── view-tasks.png
    ├── complete-task.png
    └── delete-task.png
Demo Screenshots
The screenshots folder contains examples of adding, viewing, completing and deleting tasks.
Task 'Study Python' deleted successfully!
