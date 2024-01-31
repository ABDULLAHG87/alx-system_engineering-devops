#!/usr/bin/python3
"""A python script to accessing a REST API for todo list"""

import requests
import sys
import json

if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {employeeId: []}

    for task in tasks:
        dictonary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    with open(f'{employeeId}.json', 'w') as file_name:
        json.dump(dictionary, file_name)
