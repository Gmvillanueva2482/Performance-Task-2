# To‑Do List Manager ---- Add/remove tasks; loop to display; selection for priority.
To_Do_List =[

    ]




process=input("Do you have anything to do?").lower()
while process=="no":
    if not To_Do_List:
         print("Bye then")
         break
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
    new_task=input("Do you want to add a task?")
    break

    
print(f"Total tasks in system: {len(To_Do_List)}")
if new_task=="yes".lower():
    add_task()
elif new_task=="no" and not To_Do_List:
    print("There's nothing in the list, you did everything")
elif new_task=="no":
     print("sucess")
    