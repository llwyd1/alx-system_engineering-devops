#!/usr/bin/python3
"""A module that uses a REST API"""

if __name__ == "__main__":

    import json
    import requests as r
    import sys

    userId = int(sys.argv[1])
    user = r.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
    todos = r.get(f'https://jsonplaceholder.typicode.com/todos').json()

    userTodo = {}
    taskList = []

    for task in todos:
        if task.get('userId') == userId:
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
            userTodo[userId] = taskList

    filename = f"{userId}.json"
    with open(filename, mode='w') as f:
        json.dump(userTodo, f)
