#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    
    # Define the base URL for the REST API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch the employee's information
    user_url = f"{base_url}/users/{employee_id}"
    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        print(f"Error: Could not retrieve information for employee ID {employee_id}")
        return

    employee_data = response_user.json()
    employee_name = employee_data.get('name')

    # Fetch the employee's todo list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    response_todos = requests.get(todos_url)
    if response_todos.status_code != 200:
        print(f"Error: Could not retrieve TODO list for employee ID {employee_id}")
        return


    todos_data = response_todos.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    # Print the employee todo list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python script.py <employee_id>")
            sys.exit(1)

        try:
            employee_id = int(sys.argv[1])
        except ValueError:
            print("Error: Employee ID must be an integer.")
            sys.exit(1)

        get_employee_todo_progress(employee_id)
