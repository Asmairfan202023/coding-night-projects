import click
import json
import os

TODO_FILE = "todos.json"

def load_todos():
    """Load todos from a JSON file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    """Save the list of todos to the JSON file."""
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)

@click.group()
def cli():
    """A simple Todo List CLI app."""
    pass

@cli.command()
@click.argument("task")
def add(task):
    """Add a new task to the todo list."""
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    click.echo(f'✅ Added: "{task}"')

@cli.command()
def list():
    """List all tasks."""
    todos = load_todos()
    if not todos:
        click.echo("📭 No tasks found.")
    else:
        click.echo("📝 Your Todo List:")
        for i, todo in enumerate(todos, 1):
            status = "✔️" if todo["done"] else "❌"
            click.echo(f"{i}. {status} {todo['task']}")

@cli.command()
@click.argument("index", type=int)
def remove(index):
    """Remove a task by its index."""
    todos = load_todos()
    if 0 < index <= len(todos):
        removed = todos.pop(index - 1)
        save_todos(todos)
        click.echo(f'🗑️ Removed: "{removed["task"]}"')
    else:
        click.echo("⚠️ Invalid index.")

@cli.command()
@click.argument("index", type=int)
def complete(index):
    """Mark a task as completed."""
    todos = load_todos()
    if 0 < index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        click.echo(f'✅ Marked as done: "{todos[index - 1]["task"]}"')
    else:
        click.echo("⚠️ Invalid index.")

if __name__ == "__main__":
    cli()

