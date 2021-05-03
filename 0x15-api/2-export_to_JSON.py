#!/usr/bin/python3
"""
using this REST API, for a given employee ID
returns information about his/her TODO list progress
and export data in the JSON format
"""
import json
import requests
import sys


def get_data(id):
    """ get data form API """
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(str(id))
    user = requests.get(url)
    todo = requests.get(url + 'todos')
    user_json = user.json()
    todo_json = todo.json()
    user_id = user_json.get('id')
    username = user_json.get('username')
    dic = {}
    subdict = {}
    task_list = []
    for elem in todo_json:
        subdict = {'task': elem.get('title'),
                   'completed': elem.get('completed'),
                   'username': username}
        task_list.append(subdict)
    dic[user_id] = task_list
    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump(dic, jsonfile)


if __name__ == "__main__":
    get_data(sys.argv[1])
