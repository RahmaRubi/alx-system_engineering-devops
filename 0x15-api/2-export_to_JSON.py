#!/usr/bin/python3
import requests
import sys
import json

def main(employee_id):
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
    username = employee['username']

    # Fetch TODO list
    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error fetching TODO list")
        return
    
    todos = response.json()

    # Filter TODO list for the given employee
    employee_todos = [todo for todo in todos if todo['userId'] == employee_id]

    # Prepare data for JSON export
    data = {
        str(employee_id): [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
            for todo in employee_todos
        ]
    }

    # Write data to a JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        main(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
