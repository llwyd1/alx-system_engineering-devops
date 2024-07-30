#!/usr/bin/python3
"""A module that uses a REST API"""

if __name__ == "__main__":
    import requests as r
    import sys
    import csv

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        userId = int(sys.argv[1])
        user = r.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
        todos = r.get(f'https://jsonplaceholder.typicode.com/todos/').json()
        name = user.json().get('username')

        filename = f'{userId}.csv'
        with open(filename, mode='w') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)

            for task in todos:
                if task.get('userId') == userId:
                    writer.writerow([userId, name, str(task.get('completed')),
                                     task.get('title')])
