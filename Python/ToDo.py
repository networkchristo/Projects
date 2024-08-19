tasks = []

def addTask():
    task = input("Please enter a task : ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    
def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Enter the option to delete : "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input")
    
def listTask():
    if not tasks:
        print("There is no tasks currently now.")
    else:
        print("Current tasks : ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

if __name__ == "__main__":
    # Creating an loop
    print("Welcome to the to do list ")
    while True:
        print("\n")
        print("Please select one of the following options: ")
        print("--------------------------------------------")
        print("1. Add a new task")
        print("2. Delete task")
        print("3. List all the tasks")
        print("4. Quit")

        choice = input("Enter your choice : ")
        
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTask()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again :) ")
