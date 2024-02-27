import csv
import requests
from sys import argv
import os

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        exit(1)

    user_id = argv[1]
    filename = '{}.csv'.format(user_id)

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        exit(1)

    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            num_tasks = sum(1 for row in reader) - 1  # Subtract 1 for the header row
            print(f"Number of tasks in CSV: {num_tasks}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
