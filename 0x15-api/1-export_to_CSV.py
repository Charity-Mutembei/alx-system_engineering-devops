#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress and exports it to a CSV file.
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    session = requests.Session()

    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    employee_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users'

    todos_url = f'{base_url}/{employee_id}/todos'
    employee_info_url = f'{base_url}/{employee_id}'

    todos_response = session.get(todos_url)
    employee_info_response = session.get(employee_info_url)

    todos_data = todos_response.json()
    employee_info = employee_info_response.json()

    employee_name = employee_info['name']
    user_id = employee_info['id']
    username = employee_info['username']

    completed_tasks = []

    for task in todos_data:
        task_completed_status = task['completed']
        task_title = task['title']
        completed_tasks.append([user_id,
                                username, task_completed_status, task_title])

    csv_filename = f'{user_id}.csv'

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID",
                             "USERNAME",
                             "TASK_COMPLETED_STATUS",
                             "TASK_TITLE"])
        csv_writer.writerows(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), todos_data))
    print(f"Data exported to {csv_filename}.")
