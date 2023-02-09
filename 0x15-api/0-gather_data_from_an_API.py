#!/usr/bin/python3
"""Takes an Employee ID as Input, and returns information
about their progress on their TODO list.
Uses the `JSONPlaceholder` API
"""

import requests
from sys import argv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com/'
    user_uri = '{api}/users/{ident}'.format(api=api_url, ident=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)

    #The Response to User
    response = requests.get(user_uri).json()

    #Employee Name
    emp_name = response.get('name')

    # TO-DO Response of User
    response = requests.get(todo_uri).json()

    #Calculating Total, Completed amd Uncompleted Tasks
    total_tasks = len(response)
    uncompleted = sum([tasks['completed'] is false for tasks in response])
    completed = total_tasks - uncompleted

    #Expected Output Format
    print(f"Employee {emp_name} is done with tasks({completed}/{total_tasks}):")
