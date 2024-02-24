import sys
import requests

def fetch_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    try:
        # Fetch user details
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data["name"]

        # Fetch user's todo list
        todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Calculate the number of completed tasks
        completed_tasks = [task for task in todos_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos_data)

        # Print employee's todo list progress
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_todo_list(int(employee_id))
