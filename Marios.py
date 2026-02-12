# To‑Do List Manager ---- Add/remove tasks; loop to display; selection for priority.
To_Do_List =[

    ]
process=input("Do you have anything to do?").lower()
def erase_task():
    print(To_Do_List)
    confirm=int(input("which task do you want to erase?"))
    if confirm==1:
        To_Do_List.pop(0)
        print(To_Do_List)
    elif confirm==2:
        To_Do_List.pop(1)
        print(To_Do_List)
    elif confirm==3:
        To_Do_List.pop(2)
        print(To_Do_List)
    elif confirm==4:
        To_Do_List.pop(3)
        print(To_Do_List)
def end():  
    if new_task=="yes".lower():
        add_task()
    elif new_task=="no" and not To_Do_List:
        print("There's nothing in the list, you did everything")
        quit()
    elif new_task=="no":
        print("Thanks for using")



while process=="no":
    if not To_Do_List:
         print("Bye then")
         quit()
    else:
         print(f"There are", len(To_Do_List), "Tasks left")     
while process=="yes":
    def add_task():
        print("\n--- Add a new task ---")

    # Get user input for required fields
    task= input("What's the task?: ")
    Difficulty = input("High or low difficulty?: ")
    Urgency = input("High or low urgency?: ")

    # Build the dictionary
    # Create a new dictionary with all the collected information from the user inputs
    new_task = {
        "Task": task,
        "Difficulty":Difficulty,
        "Urgency": Urgency,
        }
    for tasks in To_Do_List:
        if new_task["Task"] == task:
                print("You already have that task")
        break
         
    # Add to the list
    To_Do_List.append(new_task)
    print("Task added sucessfully.")
    print(task)
    print("-------------------------")
    print(f"Total tasks in system: {len(To_Do_List)}")
    print("new record:" , task)

    def check_task():
        print("The tasks you have in the list are:")
        print(To_Do_List)
        again=input("Do you wish to add a task")
        if again=="yes".lower:
         add_task()
        elif again=="no".lower():
            end()

    new_task=input("Do you want to add a task?")
    if new_task=="yes".lower:
         add_task()
    else:
        check=input("Do you want to check the tasks in your list?") 

    break

print(f"Total tasks in system: {len(To_Do_List)}")
if check=="yes".lower():
     check_task()
else:
     end()
erase=input("Do you want to get rid of a task?").lower()
if erase=="yes".lower():
    erase_task()
elif erase=="no".lower():
    print("bye then")
    