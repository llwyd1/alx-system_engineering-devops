#!/usr/bin/python3
"""A module that uses a REST API"""

if __name__ == "__main__":
    import requests as r
    import sys

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        userId = int(sys.argv[1])
        user = r.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
        todo = r.get(f'https://jsonplaceholder.typicode.com/todos/').json()

        my_user = user.json()
        tasks = 0
        tasks_done = 0
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
