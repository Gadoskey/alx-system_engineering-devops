#!/usr/bin/python3
"""
    The first line of all your files should be exactly
    Returns to-do list information for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    
    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)

    
