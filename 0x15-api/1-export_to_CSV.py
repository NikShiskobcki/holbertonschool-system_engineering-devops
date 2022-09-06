#!/usr/bin/python3
"""task 0"""
import requests
from sys import argv

api = 'https://jsonplaceholder.typicode.com/'
employee = requests.get(api + "users/{}".format(argv[1])).json()
employee_username = employee['username']

tasks = requests.get(api + "todos/", params={'userId': argv[1]}).json()

data = ""
filename = argv[1] + ".cvs"
with open(filename, 'w') as f:
    for task in tasks:
        data = data + "\"" + argv[1] + "\",\"" + \
               employee_username + "\",\"" + \
               str(task['completed']) + "\",\"" + task['title'] + "\"\n"
    f.write(data)
