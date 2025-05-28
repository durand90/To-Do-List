tasks = []


def addTask():
    task = input("Please enter a Task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently in list")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter Task number to delete: "))
        if taskToDelete >= 0 and taskToDelete< len(tasks):
            removed = tasks.pop(taskToDelete)
            print(f"Task {removed}  has been removed.")

        else:
            print(f"Task #{taskToDelete} was not found.")

    except ValueError:
        print("Invalid input. Please enter an acceptable value.")


if __name__ == "__main__":
    
    print("Welcome to the to do list app!")

    while True:
        print("\nPlease select one of the following options")
        print("---------------------------------------------")
        print("1. Add a new Task")
        print("2. Delete a Task")
        print("3. List a Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()

        elif choice == "2":
            deleteTask()

        elif choice == "3":
            listTasks()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please choose again.")

    print("Goodbye!")