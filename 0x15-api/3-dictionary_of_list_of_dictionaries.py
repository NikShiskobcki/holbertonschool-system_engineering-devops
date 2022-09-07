#!/usr/bin/python3
"""task 3"""

import json
import requests


if __name__ == "__main__":
    api_users = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(api_users).json()
    dictFinal = {}
    for user in users:
        aux = []
        api_tasks = "https://jsonplaceholder.typicode.com/todos"
        tasks = requests.get(api_tasks, params={"userId": user['id']}).json()
        for task in tasks:
            auxDict = {}
            auxDict["task"] = task['title']
            auxDict["completed"] = task['completed']
            auxDict["username"] = user['username']
            aux.append(auxDict)
        dictFinal[user['id']] = aux
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dictFinal, f)
