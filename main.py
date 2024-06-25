# todo_list.py

todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    print("To-Do List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def update_task():
    task_num = int(input("Enter the task number to update: "))
    new_task = input("Enter the new task: ")
    todo_list[task_num - 1] = new_task
    print(f"Task {task_num} updated!")

def delete_task():
    task_num = int(input("Enter the task number to delete: "))
    del todo_list[task_num - 1]
    print(f"Task {task_num} deleted!")

while True:
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again!")