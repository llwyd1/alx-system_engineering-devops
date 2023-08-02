#!/usr/bin/python3
"""Exports all tasks from all employees in JSON format"""

if __name__ == "__main__":

    import json
    import requests as r

    users = r.get('https://jsonplaceholder.typicode.com/users').json()
    todos = r.get('https://jsonplaceholder.typicode.com/todos').json()

    allTodo = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        allTodo[user.get('id')] = taskList

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as f:
        json.dump(allTodo, f)
