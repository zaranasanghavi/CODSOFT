import os

def add_task(tasks, detail, date_of_completion):
    tasks.append({"detail": detail, "date_of_completion": date_of_completion})

def see_list(tasks):
    if not tasks:
        print("No tasks! Press 1 to Add task")
    else:
        print("Work to be done:")
        print("Task Detail -> Due Date")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['detail']} -> {task['date_of_completion']}")

def remove_task(tasks, index_of_task):
    if 1 <= index_of_task <= len(tasks):
        del tasks[index_of_task - 1]
        print("Removed task from the list.")
    else:
        print("Invalid choice!.")

def add_to_file(tasks, file_path):
    with open(file_path, 'w') as f:
        for task in tasks:
            f.write(f"{task['detail']}|{task['date_of_completion']}\n")

def display_all(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                detail, date_of_completion = line.strip().split('|')
                tasks.append({"detail": detail, "date_of_completion": date_of_completion})
    return tasks

def main():
    tasks = []
    file_path = "tasks.txt"
    tasks = display_all(file_path)

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("What you would like to do?")

        if choice == '1':
            detail = input("Enter task detail: ")
            date_of_completion = input("Enter due date: ")
            add_task(tasks, detail, date_of_completion)
            add_to_file(tasks, file_path)
        elif choice == '2':
            see_list(tasks)
            index_of_task = int(input("Task index to be removed:"))
            remove_task(tasks, index_of_task)
            add_to_file(tasks, file_path)
        elif choice == '3':
            see_list(tasks)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Wrong input!")

if __name__ == "__main__":
    main()