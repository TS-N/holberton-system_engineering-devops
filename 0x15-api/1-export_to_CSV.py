#!/usr/bin/python3
"""using this REST API, for a given employee ID
returns information about his/her TODO list progress
and  export data in the CSV format
"""
import csv
import requests
import sys


def get_data(id):
    """ get data frim an API """
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(str(id))
    user = requests.get(url)
    todo = requests.get(url + 'todos')
    user_json = user.json()
    todo_json = todo.json()
    user_id = user_json.get('id')
    username = user_json.get('username')
    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
            datawriter = csv.writer(csvfile,
                                    delimiter=',', quoting=csv.QUOTE_ALL)
            for elem in todo_json:
                datawriter.writerow([user_id,
                                    username,
                                    elem.get('completed'),
                                    elem.get('title')])
if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_data(sys.argv[1])
