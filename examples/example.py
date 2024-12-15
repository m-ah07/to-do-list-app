from src.todo import ToDoList

# Create a new To-Do List
todo_list = ToDoList()

# Add tasks
todo_list.add_task("Learn Python")
todo_list.add_task("Build a GitHub repository")

# Display tasks
print("Current Tasks:")
todo_list.display_tasks()

# Mark a task as completed
todo_list.complete_task(0)

# Display tasks again
print("\nUpdated Tasks:")
todo_list.display_tasks()

# Delete a task
todo_list.delete_task(1)

# Save tasks to file
todo_list.save_to_file("tasks.json")

# Load tasks from file
todo_list.load_from_file("tasks.json")
print("\nTasks Loaded from File:")
todo_list.display_tasks()
