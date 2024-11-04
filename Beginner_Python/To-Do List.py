def main():
    while True:
        try:
            task = int(input("Do you wish to view your tasks, add a task, or delete a task? 1: View, 2: Add, and 3: Delete. "))
            if task == 1:
                viewTask()
                break
            elif task == 2:
                addTask()
                break
            elif task == 3:
                deleteTask()
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3. ")
        except ValueError:
            print("Invalid input. Please enter a number 1, 2, or 3. ")

def viewTask():
    print("Here is your To-Do List: ")
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your To-Do list is empty. ")
    main()

    

def addTask():
    tasks.append(str(input("Whats the task that you would like to add? ")))
    while True:
        try:
            again = int(input("Would you like to add another task? 1: Yes, 2: No "))
            if again == 1:
                addTask()
                break
            elif again == 2:
                viewTask()
                break
            else:
                print("Invalid input. Please enter 1, or 2 ")
        except ValueError:
            print("Invalid input. Please enter a number 1, or 2. ")



def deleteTask():
    while True:
        if not tasks:
            print("You don't have any tasks to delete. Please add one first. ")
            main()
            break
        try:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            delete = int(input("Which task would you like to delete? Enter the number ")) - 1
            tasks.pop(delete)
            break
        except IndexError:
            print("Invalid input. Please enter a number that corresponds to a task")
        except ValueError:
            print("Invalid input. Please enter a valid number. ")

    while True:
        try:
            again = int(input("Would you like to delete another task? 1: Yes, 2: No "))
            if again == 1:
                deleteTask()
                break
            elif again == 2:
                viewTask()
                break
            else:
                print("Invalid input. Please enter 1, or 2 ")
        except ValueError:
            print("Invalid input. Please enter a number 1, or 2. ")


if __name__ == '__main__':
    tasks = []
    main()