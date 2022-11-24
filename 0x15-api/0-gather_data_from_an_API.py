#!/usr/bin/python3
"""A module that uses a REST API"""
import requests as r
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user = r.get(f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')
        todo = r.get(f'https://jsonplaceholder.typicode.com/todos/').json()

        my_user = user.json()
        tasks = 0
        tasks_done = 0
        userId = int(sys.argv[1])
        titles = ""
        i = 0

        while i < len(todo):
            if todo[i]['userId'] == userId and todo[i]['completed'] is True:
                tasks_done += 1
                tasks += 1
                titles += f"\t {todo[i]['title']}\n"
            elif todo[i]['userId'] == userId and todo[i]['completed'] is False:
                tasks += 1
            i += 1

    print("Employee {} is done with tasks({}/{}):".format(my_user.get('name'),
                                                          tasks_done, tasks))
    print(titles, end="")
