import json

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.title} - {task.description} [{task.status}]")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            tasks_json = [task.__dict__ for task in self.tasks]
            json.dump(tasks_json, file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_json = json.load(file)
                self.tasks = [Task(task['title'], task['description'], task['status']) for task in tasks_json]
        except FileNotFoundError:
            print("File not found. Creating a new to-do list.")
        except json.JSONDecodeError:
            print("Invalid data in the file. Creating a new to-do list.")

def main():
    print("Welcome to the ToDo List App!")
    todo_list = ToDoList()

    filename = "tasks.json"
    todo_list.load_tasks(filename)

    while True:
        print("\nSelect an option:")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. View all tasks")
        print("4. Save tasks to file")
        print("5. Exit")

        choice = input("Enter the option number: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
            print("Task added successfully.")
        elif choice == "2":
            title = input("Enter task title to delete: ")
            if todo_list.delete_task(title):
                print("Task deleted successfully.")
            else:
                print("Task not found.")
        elif choice == "3":
            print("\nCurrent tasks:")
            todo_list.view_tasks()
        elif choice == "4":
            todo_list.save_tasks(filename)
            print("Tasks saved to file successfully.")
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
