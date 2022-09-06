#!/usr/bin/python3
"""task 2"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    api = 'https://jsonplaceholder.typicode.com/'
    employee = requests.get(api + "users/{}".format(argv[1])).json()
    employee_username = employee['username']

    tasks = requests.get(api + "todos/", params={'userId': argv[1]}).json()

    filename = argv[1] + ".json"

    lst = []
    for task in tasks:
        dictAux = {}
        dictAux["task"] = task['title']
        dictAux["completed"] = task['completed']
        dictAux["username"] = employee_username
        lst.append(dictAux)
    aux = {}
    aux[argv[1]] = lst
    with open(filename, 'w') as f:
        json.dump(aux, f)
