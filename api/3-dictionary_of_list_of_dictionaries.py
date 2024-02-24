import json
import requests


def fetch_todo():
    """
    Fetches TODO data from a mock API.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = response.json()
    return todos


def group_tasks_by_user(tasks):
    """
    Groups tasks by user ID.
    """
    grouped_tasks = {}
    for task in tasks:
        user_id = task['userId']
        if user_id not in grouped_tasks:
            grouped_tasks[user_id] = []
        grouped_tasks[user_id].append({
            'username': task['username'],
            'task': task['title'],
            'completed': task['completed']
        })
    return grouped_tasks


def export_to_json(grouped_tasks):
    """
    Exports grouped tasks to JSON file.
    """
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(grouped_tasks, json_file, indent=4)


def main():
    # Fetch TODO data
    todos = fetch_todo()

    # Group tasks by user ID
    grouped_tasks = group_tasks_by_user(todos)

    # Export to JSON
    export_to_json(grouped_tasks)

    # Test if all users exist in the output
    all_users_found = len(grouped_tasks) == 10

    # Test if all tasks are assigned to the correct user IDs
    user_ids = [task['userId'] for task in todos]
    user_ids_in_output = list(grouped_tasks.keys())
    user_tasks_output_ok = user_ids == user_ids_in_output

    print("All users found:", "OK" if all_users_found else "Failed")
    print("User ID and Tasks output:", "OK" if user_tasks_output_ok else "Failed")


if __name__ == "__main__":
    main()
