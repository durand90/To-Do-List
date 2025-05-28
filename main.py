tasks = []


def addTask():
    task = input("Please enter a Task: ")
    tasks.append(task)
    print("f.Task '{task}' added to the list.")

def deleteTask():
    task = 


if __name__ == "--main__":
    
    print("Welcome to the to do list app!")

    while True:
        print("\n")
        print("Please select one of the following options")
        print("---------------------------------------------")
        print("1. Add a new Task")
        print("2. Delete a Task")
        print("3. List a Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()

        elif(choice == "2"):
            deleteTask()

        elif(choice == "3"):
            listTAsk()

        elif(choice == "4"):
            break

        else:
            print("Invalid choice. Please choose again.")

    print("Goodbye!")