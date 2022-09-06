#!/usr/bin/python3
"""task 1"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    api = 'https://jsonplaceholder.typicode.com/'
    employee = requests.get(api + "users/{}".format(argv[1])).json()
    employee_username = employee['username']

    tasks = requests.get(api + "todos/", params={'userId': argv[1]}).json()

    filename = argv[1] + ".csv"
    with open(filename, 'w') as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([argv[1], employee_username,
                            task['completed'], task['title']])
