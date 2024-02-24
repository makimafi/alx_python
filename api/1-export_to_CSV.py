import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetching data from the API
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    tasks = response.json()

    # Writing data to CSV file
    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for task in tasks:
            writer.writerow([user_id, task['userId'], task['completed'], task['title']])

    print(f'Data exported to {filename}')
