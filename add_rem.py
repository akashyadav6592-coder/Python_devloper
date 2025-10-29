# Initialize an empty task list
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

# Function to remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: {task}")
    else:
        print(f"Task not found: {task}")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

# Example usage
add_task("Buy groceries")
add_task("Finish homework")
view_tasks()
remove_task("Finish homework")
view_tasks()
