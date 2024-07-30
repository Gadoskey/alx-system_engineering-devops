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

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [sys.argv[1], username, todo.get("completed"), todo.get("title")]
        ) for todo in todos]
