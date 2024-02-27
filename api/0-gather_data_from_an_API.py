import requests
import sys

def fetch_employee_data(employee_id):
    try:
        # Fetch employee details
        employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        employee_data = employee_response.json()
        employee_name = employee_data['name']

        # Fetch TODO list
        todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
        todo_list = todo_response.json()

        # Calculate completed tasks
        completed_tasks = [task for task in todo_list if task['completed']]

        # Display progress
        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todo_list)}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")  # Ensure one tabulation and one space before the task title

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    fetch_employee_data(employee_id)
