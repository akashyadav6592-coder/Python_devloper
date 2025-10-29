# File to store tasks
TASK_FILE = "tasks.txt"

# Function to add a task
def add_task(task):
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")
    print(f"Added task: {task}")

# Function to remove a task
def remove_task(task):
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()
    with open(TASK_FILE, "w") as file:
        found = False
        for line in tasks:
            if line.strip() != task:
                file.write(line)
            else:
                found = True
        if found:
            print(f"Removed task: {task}")
        else:
            print(f"Task not found: {task}")

# Function to view all tasks
def view_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            if tasks:
                print("Your tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("No tasks found.")
    except FileNotFoundError:
        print("No task file found. Start by adding a task.")

# Example usage
add_task("Buy groceries")
add_task("Finish homework")
view_tasks()
remove_task("Finish homework")
view_tasks()
