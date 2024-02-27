import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        exit(1)

    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    try:
        response = requests.get(user_url)
        user_data = response.json()
        username = user_data.get('username')
    except requests.exceptions.RequestException as e:
        print('Error fetching user data:', e)
        exit(1)

    try:
        response = requests.get(url)
        tasks = response.json()
    except requests.exceptions.RequestException as e:
        print('Error fetching tasks:', e)
        exit(1)

    filename = '{}.csv'.format(user_id)

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for task in tasks:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })

    print(f'Tasks exported to {filename}')
