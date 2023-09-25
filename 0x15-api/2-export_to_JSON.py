#!/usr/bin/python3
"""
This script will use the REST API, take an employee's ID
and return their information on the progress of their
TO-DO list. It will also export the data in JSON format.
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
    employee_name = employee_info_response.json()['username']

    completed_tasks = [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        for task in todos_data
    ]

    user_data = {employee_id: completed_tasks}

    output_file = f'{employee_id}.json'
    with open(output_file, 'w') as json_file:
        json.dump(user_data, json_file, indent=4)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), todos_data))

