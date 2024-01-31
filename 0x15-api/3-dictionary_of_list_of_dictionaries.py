#!/usr/bin/python3
"""A python script to accessing a REST API for todo list"""

import json
import requests
import sys


if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(baseUrl)
    users = response.json()

    dictionary = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        baseUrl = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        baseUrl = baseUrl + '/todos'
        response = requests.get(baseUrl)
        tasks = response.json()
        dictionary[user_id] = []

        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    with open('todo_all_employees.json', 'w') as filename:
        json.dump(dictionary, filename)
