#!/usr/bin/python3
import requests
import sys
import csv

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
    employee_name = employee['name']

    # Fetch TODO list
    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error fetching TODO list")
        return
    
    todos = response.json()

    # Filter TODO list for the given employee
    employee_todos = [todo for todo in todos if todo['userId'] == employee_id]

    # Prepare CSV file name
    csv_file_name = f"{employee_id}.csv"

    # Open CSV file for writing
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        
        # Write each TODO item as a new row
        for todo in employee_todos:
            writer.writerow([employee_id, employee_name, todo['completed'], todo['title']])
    
    print(f"Data has been exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        main(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
