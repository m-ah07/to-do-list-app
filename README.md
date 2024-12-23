# To-Do List App

A simple Python-based command-line tool for managing tasks. It allows users to add, view, update, and delete tasks while storing task data in a local file.

## 🚀 Features
- Add tasks to the list.
- Mark tasks as completed.
- Delete tasks from the list.
- Save and load tasks from a JSON file.

## 📂 Directory Structure
```plaintext
to-do-list-app/
├── src/
│   └── todo.py
├── examples/
│   └── example.py
├── .gitignore
├── LICENSE
└── README.md
```

## 🔧 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/marwan-ahmed-23/to-do-list-app.git
    ```

2. Navigate to the project directory:
    
    ```bash
    cd to-do-list-app
    ```

## 📖 Usage

1. Run the example script:

    ```bash
    python examples/example.py
    ```

2. Explore the `todo.py` file to customize functionality.

## Example

Here’s an example of how to use the `ToDoList` class:

```bash
from src.todo import ToDoList

# Create a new To-Do List
todo_list = ToDoList()

# Add tasks
todo_list.add_task("Learn Python")
todo_list.add_task("Build a GitHub repository")

# Display tasks
todo_list.display_tasks()
```

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 🌟 Stay Connected
Feel free to star ⭐ this repository if you find it helpful!
