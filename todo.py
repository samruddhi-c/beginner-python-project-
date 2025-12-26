tasks = []

def show_menu():
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    new_task = input("Enter task: ")
    tasks.append(new_task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def delete_task():
    view_tasks()
    if tasks:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number!")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice! Try again.")
