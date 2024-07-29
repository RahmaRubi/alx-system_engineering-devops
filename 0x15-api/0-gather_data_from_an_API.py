#!/usr/bin/python3
"""
python script gathers data from a rest API
"""


import requests
import sys


def main(employee_id):
    """endpoints"""
    # API URLs
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos'

    # Fetch employee information
    response = requests.get(employee_url)
    if response.status_code != 200:
        print("Employee not found")
        return

    employee = response.json()
    employee_name = employee['name']

    # Fetch TODO list
    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error fetching TODO list")
        return

    todos = response.json()

    # Filter TODO list for the given employee
    employee_todos = [todo for todo in todos if todo['userId'] == employee_id]

    # Calculate progress
    total_tasks = len(employee_todos)
    done_tasks = len([todo for todo in
                      employee_todos if todo['completed']])
    completed_tasks_titles = [todo['title']
                              for todo in employee_todos if todo['completed']]

    # Output
    print(f'Employee {employee_name}'
          'is done with tasks({done_tasks}/{total_tasks}):')
    for title in completed_tasks_titles:
        print(f'     {title}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        main(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
