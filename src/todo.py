import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """Add a new task to the list."""
        task = {"description": description, "completed": False}
        self.tasks.append(task)

    def display_tasks(self):
        """Display all tasks in the list."""
        if not self.tasks:
            print("No tasks available.")
            return

        for idx, task in enumerate(self.tasks):
            status = "✔️" if task["completed"] else "❌"
            print(f"{idx + 1}. {task['description']} - {status}")

    def complete_task(self, index):
        """Mark a task as completed."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        """Delete a task from the list."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task index.")

    def save_to_file(self, filename):
        """Save tasks to a JSON file."""
        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_from_file(self, filename):
        """Load tasks from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("File not found. Starting with an empty task list.")
