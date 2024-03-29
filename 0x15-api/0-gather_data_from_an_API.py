#!/usr/bin/python3
"""A python script to accessing a REST API for todo list"""

import requests
import sys

if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print(f"Employee {employeeName} is done with tasks({done}/{len(tasks)}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")
