#!/usr/bin/python3
"""using this REST API, for a given employee ID
returns information about his/her TODO list progress
"""
import requests
import sys


def get_data(id):
    """ get data from an API """
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(str(id))
    user = requests.get(url)
    todo = requests.get(url + 'todos')
    user_json = user.json()
    todo_json = todo.json()
    task_done = 0
    tasks = 0
    task_list_completed = []
    for elem in todo_json:
        if elem.get('completed') is True:
            task_done += 1
            s = elem.get('title')
            s = '\t ' + s
            task_list_completed.append(s)
        tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
                                                         user_json.get('name'),
                                                         task_done, tasks))
    for i in task_list_completed:
        print(i)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_data(sys.argv[1])
