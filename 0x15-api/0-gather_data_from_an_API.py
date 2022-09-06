#!/usr/bin/python3
"""task 0"""
import requests
from sys import argv

api = 'https://jsonplaceholder.typicode.com/'
employee = requests.get(api + "users/{}".format(argv[1])).json()
employee_name = employee['name']

tasks = requests.get(api + "todos/", params={'userId': argv[1]}).json()

taskCount = len(tasks)
tasksDone = 0

for task in tasks:
    if task['completed'] is True:
        tasksDone += 1

print("Employee {} is done with tasks({}/{})".format(employee_name,
                                                     tasksDone, taskCount))
for task in tasks:
    if task['completed'] is True:
        print("\t " + task['title'])
