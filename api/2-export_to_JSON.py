#!/usr/bin/python3
""" Export to JSON """
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get('username')

    tasks = []
    for todo in todos_data:
        task = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        tasks.append(task)

    json_data = {user_id: tasks}

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(json_data, json_file)
