# Simple To-Do List Application (CLI Version)
# CodSoft Internship Task
# Made using Python

import json
import os

file_name = "tasks_cli.json"

# -------- Load saved tasks --------
def load_tasks():
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    return []

# -------- Save tasks --------
def save_tasks():
    with open(file_name, "w") as f:
        json.dump(tasks, f)

# -------- Show all tasks --------
def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    print("\nYour Tasks:")
    for i in range(len(tasks)):
        status = "✔" if tasks[i]["done"] else "✘"
        print(f"{i+1}. [{status}] {tasks[i]['title']}")
    print()

# -------- Add task --------
def add_task():
    task = input("Enter new task: ").strip()

    if task == "":
        print("Task cannot be empty!\n")
        return

    tasks.append({"title": task, "done": False})
    save_tasks()
    print("Task added successfully!\n")

# -------- Mark task as complete --------
def mark_complete():
    show_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num - 1]["done"] = True
        save_tasks()
        print("Task marked as completed!\n")
    except:
        print("Invalid task number!\n")

# -------- Delete task --------
def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks()
        print(f"Task '{removed['title']}' deleted!\n")
    except:
        print("Invalid task number!\n")


# -------- Main Program --------
tasks = load_tasks()

while True:
    print("====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye! ")
        break
    else:
        print("Invalid choice! Please try again.\n")
