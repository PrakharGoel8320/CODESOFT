# To-Do List App Program.This program allows users to create, view, mark as completed, delete, and filter tasks. It also saves the tasks to a file and loads them when the program starts.

def create_task(tasks): # Function to create a new task.
    try:
        name=input("Enter task name: ")
        number=int(input("Enter task number: "))
        description=input("Enter task description: ")
        duedate=input("Enter task due date (YYYY-MM-DD): ")
        priority=input("Enter task priority (High/Medium/Low): ")
        
        for task in tasks: # Check for duplicates by task number
            if task["Task_number"] == number:
                print("A task with this number already exists. Please enter a unique task number.")
                return  # Exit without saving
        
    except ValueError:
        print("Invalid Input! Please enter valid values.")
        main() # Call the main function to restart the program.
        
    task={
        "Task_name": name,
        "Task_number": number,
        "Task_description": description,
        "Task_duedate": duedate,
        "Task_priority": priority,
        "Task_completed": False
    }
    
    tasks.append(task) # Append the new task to the tasks list.

    with open("tasksfile.txt", "a") as f:
       
        for i in tasks:
           
            line = i["Task_name"] + " | " + str(i["Task_number"]) + " | " + i["Task_description"] + " | " + i["Task_duedate"] + " | " + i["Task_priority"] + " | " + str(i["Task_completed"]) + "\n"
            f.write(line) # Write the task details to the file.
    
    print("Task saved successfully!")


def view_task(tasks): # Function to view all tasks.
    
    if len(tasks) == 0:
       
        print("No tasks available.")
    
    else:
       
        print("Your tasks are:")
        
        for i in tasks:
           
            print("Task Name: ", i["Task_name"])
            print("Task Number: ", i["Task_number"])
            print("Task Description: ", i["Task_description"])
            print("Task Due Date: ", i["Task_duedate"])
            print("Task Priority: ", i["Task_priority"])
            print("Task Status: ", "Done" if i["Task_completed"] else "Pending")
            print("\n")


def task_completed(tasks): # Function to mark a task as completed.
    
    task_number = int(input("Enter the task number to mark as completed: "))
    
    found = False
    
    for i in tasks:
       
        if i["Task_number"] == task_number:
           
            i["Task_completed"] = True
            print("Task marked as completed!")
            
            found = True
            
            break
        
    if not found:
        
        print("Task not found! Enter a valid task number.")
    
    with open("tasksfile.txt", "w") as f:
        
        for i in tasks:
            
            line = i["Task_name"] + " | " + str(i["Task_number"]) + " | " + i["Task_description"] + " | " + i["Task_duedate"] + " | " + i["Task_priority"] + " | " + str(i["Task_completed"]) + "\n"
            f.write(line) # Write the updated task details to the file.
  
        
def delete_task(tasks): # Function to delete a task.
    
    task_number = int(input("Enter the task number to delete: "))
    
    for i in tasks:
        
        if i["Task_number"] == task_number:
            
            tasks.remove(i)
            print("Task deleted successfully!")
            break
        
        else:
            
            print("Task not found! Enter a valid task number.")
    
    with open("tasksfile.txt", "w") as f:
        
        for i in tasks:
           
            line = i["Task_name"] + " | " + str(i["Task_number"]) + " | " + i["Task_description"] + " | " + i["Task_duedate"] + " | " + i["Task_priority"] + " | " + str(i["Task_completed"]) + "\n"
            f.write(line) # Write the updated task details to the file.


def filter_tasks(tasks):  # Function to filter tasks based on priority and status.

    ch = input("Select filter (Priority/Status): ")

    if ch.lower() == "priority":
        
        found = 0 
        
        priority = input("Enter the priority to filter (High/Medium/Low): ") # Ask user for priority to filter.

        for i in tasks:
            
            if i["Task_priority"].lower() == priority.lower():
                
                print("Task Name: ", i["Task_name"])
                print("Task Number: ", i["Task_number"])
                print("Task Description: ", i["Task_description"])
                print("Task Due Date: ", i["Task_duedate"])
                print("Task Status: ", "Done" if i["Task_completed"] else "Pending")
                print("\n")
                
                found = 1  

        if found == 0:
            
            print("No tasks available with the priority", priority)

    elif ch.lower() == "status":
        
        status = input("Enter the status to filter (Done/Pending): ")
        
        found = 0  

        if status.lower() == "done":
            
            for i in tasks:
                
                if i["Task_completed"]:
                    
                    print("Task Name: ", i["Task_name"])
                    print("Task Number: ", i["Task_number"])
                    print("Task Description: ", i["Task_description"])
                    print("Task Due Date: ", i["Task_duedate"])
                    print("Task Priority: ", i["Task_priority"])
                    print("\n")
                    
                    found = 1 

            if found == 0:
                
                print("No tasks available with the status 'Done'.")

        elif status.lower() == "pending":
            
            for i in tasks:
                
                if not i["Task_completed"]:
                    
                    print("Task Name: ", i["Task_name"])
                    print("Task Number: ", i["Task_number"])
                    print("Task Description: ", i["Task_description"])
                    print("Task Due Date: ", i["Task_duedate"])
                    print("Task Priority: ", i["Task_priority"])
                    print("\n")
                    
                    found = 1

            if found == 0:
                
                print("No tasks available with the status 'Pending'.")

        else:
            
            print("Invalid status! Please enter 'Done' or 'Pending'.")

    else:
        
        print("Invalid filter! Please enter 'Priority' or 'Status'.")


def task_update(tasks):  # Function to update an existing task.
    
    task_number = int(input("Enter the task number to update: "))
    
    found = False

    for task in tasks:
        
        if task["Task_number"] == task_number:
            
            found = True
            
            print("Current Task Details:")
            print("1. Task Name:", task["Task_name"])
            print("2. Description:", task["Task_description"])
            print("3. Due Date:", task["Task_duedate"])
            print("4. Priority:", task["Task_priority"])
            
            # Ask what the user wants to update.
            
            print("Enter new values (or press Enter to keep the same):")
            new_name = input("New Task Name: ")
            new_description = input("New Description: ")
            new_duedate = input("New Due Date (YYYY-MM-DD): ")
            new_priority = input("New Priority (High/Medium/Low): ")

            if new_name:
                
                task["Task_name"] = new_name
                
            if new_description:
                
                task["Task_description"] = new_description
                
            if new_duedate:
                
                task["Task_duedate"] = new_duedate
                
            if new_priority:
                
                task["Task_priority"] = new_priority

            print("Task updated successfully!")
            break

    if not found:
        
        print("Task not found! Enter a valid task number.")
        return

    with open("tasksfile.txt", "w") as f:     # Write the updated tasks list back to the file
       
        for t in tasks:
            
            line = t["Task_name"] + " | " + str(t["Task_number"]) + " | " + t["Task_description"] + " | " + t["Task_duedate"] + " | " + t["Task_priority"] + " | " + str(t["Task_completed"]) + "\n"
            f.write(line)



def load_tasks(): # Function to load tasks from a file.
    
    tasks = []
    
    try:
        
        with open("tasksfile.txt", "r") as f:
            
            for line in f:
                
                task = line.strip().split(" | ")
                
                if len(task) == 6:
                    
                    task_dict = {
                        "Task_name": task[0],
                        "Task_number": int(task[1]),
                        "Task_description": task[2],
                        "Task_duedate": task[3],
                        "Task_priority": task[4],
                        "Task_completed": task[5] == "True"
                    }
                    
                    tasks.append(task_dict) # Append the loaded task to the tasks list.
                
    except:
        
        pass # If the file does not exist, do nothing.  
    
    return tasks


def main(): # Main function to run the To-Do List App.
        
        tasks = load_tasks() # Load tasks from the file.
        
        while True:
            
            print("Welcome to the To-Do List App!")
            print("Select operation to continue:")
            print("1. Create Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Filter Tasks")
            print("6. Update Task")
            print("7. Exit")
            
            choice = input("Enter choice (1/2/3/4/5/6): ")
            
            if choice == '1':
                
                create_task(tasks) # Call the create_task function.
                
            elif choice == '2':
                
                view_task(tasks) # Call the view_task function.
                
            elif choice == '3':
                
                task_completed(tasks) # Call the task_completed function.
                
            elif choice == '4':
                
                delete_task(tasks) # Call the delete_task function.
                
            elif choice == '5':
                
                filter_tasks(tasks) # Call the filter_tasks function.
                
            elif choice == '6': # Call the task_update function.
                
                task_update(tasks)
                
            elif choice == '7':
                
                print("Thank you for using the To-Do List App!")
                print("Goodbye!")
                break # Exit the loop and end the program.
                
            else:
               
                print("Invalid Choice! Please select a valid operation.")

if __name__ == "__main__": # Check if the script is being run directly.
   
    main() # Call the main function to run the To-Do List App.