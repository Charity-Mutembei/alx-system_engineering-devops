#!/usr/bin/python3
"""
Scrit that exports data in Json format
"""

import json
import requests

if __name__ == "__main__":
    # Import necessary libraries
    import json
    import requests

    # Fetch user data from the API
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = users_response.json()

    # Fetch TODO tasks from the API
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_data = todos_response.json()

    # Create a dictionary to store all TODO tasks for each user
    all_tasks_by_user = {}

    # Iterate through each user
    for user in users_data:
        user_id = user.get('id')
        user_username = user.get('username')

        # Initialize a list to store tasks for the current user
        user_tasks = []

        # Iterate through all tasks to find tasks assigned to the current user
        for task in todos_data:
            if task.get('userId') == user_id:
                task_dict = {
                    "username": user_username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                user_tasks.append(task_dict)

        # Assign the list of tasks to the user ID in the dictionary
        all_tasks_by_user[user_id] = user_tasks

    # Write the collected data to a JSON file
    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(all_tasks_by_user, json_file)
