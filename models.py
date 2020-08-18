from datetime import datetime
from typing import Optional, Union

import json, os

class User(object):
    """Класс пользователя, принимает в качестве полей:
    1. Имя пользователя (str) - обязательный
    2. Возраст (int) - опционально, можно не вводить, тогда будет None"""

    def __init__(self, name: str, age: Optional[int]=None):
        self.id = self.get_new_id
        self.name = name
        self.age = age


    def __str__(self):
        return f'{self.name} (id: {self.id})'


    @property
    def get_new_id(self):
        """id_counter содержит последний присвоенный id
        Считать последний присвоенный id
        Присвоить новому пользователю id + 1
        Записать новый id в файл"""
        with open('id_counter', 'r') as read_last_id:
            id = int(read_last_id.read()) + 1
        with open('id_counter', 'w') as write_new_last_id:
            write_new_last_id.write(str(id))
        return id


    @staticmethod
    def write_in_file_users(data):
        with open('users.json', 'w') as dump_json:
            json.dump(data, dump_json)


    @staticmethod
    def get_users():
        """Возвращает список всех пользователей"""
        with open('users.json', 'r') as load_file:
            return json.load(load_file)


    @staticmethod
    def get_user_by_id(user_id: int):
        """Возвращает пользователя по его id"""
        with open('users.json', 'r') as load_file:
            return [user for user in json.load(load_file) \
                if user['id'] == user_id]


    def create_user(self):
        """Создаёт нового пользователя"""

        with open('users.json', 'r') as load_file:
            data = json.load(load_file)

        user_data = {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'creation_datetime': datetime.now().strftime('%d.%m.%Y %H:%M'),
            'last_update_datetime': None
        }

        data.append(user_data)

        self.write_in_file_users(data)
