#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress and exports it to a CSV file.
"""
import csv
import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users'

    todos_url = f'{base_url}/{employee_id}/todos'
    employee_info_url = f'{base_url}/{employee_id}'

    session = requests.Session()

    employee_response = session.get(todos_url)
    employee_name_response = session.get(employee_info_url)

    employee_data = employee_response.json()
    employee_username = employee_name_response.json()['username']

    total_completed_tasks = sum(1 for task in employee_data
                                if task['completed'])

    csv_filename = f'{employee_id}.csv'

    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID",
                             "USERNAME",
                             "TASK_COMPLETED_STATUS",
                             "TASK_TITLE"])
        for task in employee_data:
            task_completed_status = task['completed']
            task_title = task['title']
            csv_writer.writerow([employee_id,
                                 employee_username,
                                 task_completed_status,
                                 task_title])

    print(f"Data exported to {csv_filename}.")
