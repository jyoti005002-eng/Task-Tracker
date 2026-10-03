"""The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks

Mark a task as in progress or done

List all tasks

List all tasks that are done

List all tasks that are not done

List all tasks that are in progress

Here are some constraints to guide the implementation:

You can use any programming language to build this project.

Use positional arguments in command line to accept user inputs.

Use a JSON file to store the tasks in the current directory.

The JSON file should be created if it does not exist.

Use the native file system module of your programming language to interact with the JSON file.

Do not use any external libraries or frameworks to build this project.

Ensure to handle errors and edge cases gracefully.

""" 

tasks = []

def show_menu():
    print(" ---TASK TRACKER---\n")
    print("1. Add a task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task : ")
    tasks.append({"task":task , "done":False}) 
    print(f"task '{task}' added ! ")  

def view_task():
    if not tasks:
        print("No tasks available ")
        return 
    print("\n Your Tasks : ")
    for index , task in enumerate(tasks , start = 1):
        status = "✅ " if task["done"] else "❌ "
        print(f"{index}.{task['task']} [{status}]")

def mark_task_done():
    view_task()
    if not tasks:
        return

    try:
        index = int(input("Enter task number to mark as done:")) -1 
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True 
            print("Marked as done !")

        else:
            print("Invalid task number !")

    except ValueError:
        print("Please enter a valid number !")

def delete_task():
    view_task()
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete :")) -1 
        if 0 <= index <len(tasks):
            removed = tasks.pop(index)
            print(f" Deleted task : {removed['task']}")
        else:
            print("Invalid task number !")

    except ValueError :
        print("Please enter a valid number !")

while True :
    show_menu()
    choice = input("Choose an optio (1 - 5 ) :")

    if choice == "1" :
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye !")
        break

    else:
        print("Invalid choice . Try again !!")