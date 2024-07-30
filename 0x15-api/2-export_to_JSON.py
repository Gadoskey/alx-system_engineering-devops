#!/usr/bin/python3
"""
    The first line of all your files should be exactly
    Returns to-do list information for a given employee ID.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(sys.argv[1]), "w") as json_file:
        json.dump({user_id: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
            } for todo in todos]}, json_file)
