from datetime import datetime

import json, os

class User(object):

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


    def __str__(self):
        return f'{self.name} ({self.id})'


    @staticmethod
    def get_users():
        """Возвращает список всех пользователей"""
        with open('FlaskAPI/users.json', 'r') as load_file:
            return json.load(load_file)


    @staticmethod
    def get_user_by_id(user_id):
        with open('FlaskAPI/users.json', 'r') as load_file:
            return [user for user in json.load(load_file) \
                if user['id'] == user_id][0]


    def create_user(self):
        with open('users.json', 'r') as load_file:
            data = json.load(load_file)
        user_data = {
            'id': self.id,
            'name': self.name,
            'creation_datetime': datetime.now().strftime('%d.%m.%Y %H:%M'),
            'last_change_datetime': None
        }

        data.append(user_data)

        with open('users.json', 'w') as dump_json:
            json.dump(data, dump_json)
