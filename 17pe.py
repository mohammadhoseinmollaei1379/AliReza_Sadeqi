


import os

TODO_FILE = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            tasks = [line.strip() for line in file]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {task}")

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


add_task("python practice")
list_tasks()