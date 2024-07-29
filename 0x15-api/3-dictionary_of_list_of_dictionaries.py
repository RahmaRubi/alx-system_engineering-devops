#!/usr/bin/python3
import requests
import json

def main():
    # API URLs
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    # Fetch users
    response = requests.get(users_url)
    if response.status_code != 200:
        print("Error fetching users")
        return
    
    users = response.json()

    # Fetch TODO list
    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Error fetching TODO list")
        return
    
    todos = response.json()

    # Structure data
    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos if todo['userId'] == user_id
        ]
        data[user_id] = user_tasks

    # Write to JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    main()
