#!/usr/bin/python3
"""Export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()

    user_tasks = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
        response = requests.get(url)
        tasks = response.json()

        user_tasks[user_id] = []
        for task in tasks:
            task_dict = {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed'),
            }
            user_tasks[user_id].append(task_dict)

    # Write data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)
