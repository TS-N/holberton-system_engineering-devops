#!/usr/bin/python3
"""
using this REST API, for all employees
returns information about their TODO list progress
and export data in the JSON format
"""
import json
import requests
import sys


def get_data():
    """ get data form API """
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()
    dic = {}
    for user in users:
        l = []
        user_id = user.get('id')
        username = user.get('username')
        todos = requests.get("{}/{}/todos".format(url, user_id)).json()
        for todo in todos:
            subdict = {'task': todo.get('title'),
                       'completed': todo.get('completed'),
                       'username': username}
            l.append(subdict)
        dic[user_id] = l
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(dic, jsonfile)


if __name__ == "__main__":
    get_data()
