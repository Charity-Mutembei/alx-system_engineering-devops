#!/usr/bin/python3
"""
This script will use the REST API, taken an employees ID
and return their information on the progress of their
TO-DO list
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    session = requests.Session()

    employee_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users'

    todos_url = f'{base_url}/{employee_id}/todos'
    employee_info_url = f'{base_url}/{employee_id}'

    todos_response = session.get(todos_url)
    employee_info_response = session.get(employee_info_url)

    todos_data = todos_response.json()
    employee_name = employee_info_response.json()['name']

    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t " + task.get('title'))
