my_tasks = []

while True:
    print("\n--- MENU ---")
    print("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. EXIT")
    
    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        task = input("Enter a task: ")
        my_tasks.append(task)
        print("Task Added Successfully.")
        
    elif choice == 2:
        if not my_tasks:
            print("No Task Available.")
        else:
            print("\nYour Tasks:")
            for i, each_task in enumerate(my_tasks, start=1):
                print(f"{i}. {each_task}")
                
    elif choice == 3:
        print("Thank you for using the To-Do List!")
        break
        
    else:
        print("Invalid Choice. Please choose 1, 2, or 3.")