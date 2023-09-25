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
    # Create a session for making requests
    session = requests.Session()

    # Get the employee ID from the command line arguments
    employee_id = argv[1]

    # Define the base URL
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'

    # Define the specific endpoints for tasks and name
    tasks_endpoint = 'todos'
    name_endpoint = ''

    # Construct the URLs for employee tasks and name
    tasks_url = base_url.format(employee_id) + '/' + tasks_endpoint
    name_url = base_url.format(employee_id) + '/' + name_endpoint

    # Fetch employee tasks and name from the API
    tasks_response = session.get(tasks_url)
    name_response = session.get(name_url)

    # Parse the JSON responses
    tasks_data = tasks_response.json()
    username = name_response.json()['username']

    # Initialize an empty list to store task information
    task_list = []

    # Create a dictionary to store user data
    user_data = {}

    # Iterate through tasks and append information to the task_list
    for task in tasks_data:
        task_list.append(
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username,
            }
        )

    # Assign the task_list to the user_data with the user ID as the key
    user_data[employee_id] = task_list

    # Create the JSON filename
    json_filename = employee_id + ".json"

    # Write the user data to a JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(user_data, json_file)
