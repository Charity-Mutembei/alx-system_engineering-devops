#!/usr/bin/python3
"""
This script will use the REST API, taken an employees ID
and return their information on the progress of their
TO-DO list
"""

import requests
import json
import sys


def get_employee_info(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    id_url = f'{base_url}/{employee_id}/todos'
    name_url = f'{base_url}/{employee_id}'

    session = requests.Session()
    employee_data = session.get(id_url).json()
    employee_name = session.get(name_url).json()['name']

    total_tasks = sum(1 for task in employee_data if task['completed'])

    completed_tasks_message = (
        f"Employee {employee_name} is done with tasks "
        f"({total_tasks}/{len(employee_data)}):"
    )
    print(completed_tasks_message)

    for task in employee_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_info(employee_id)
