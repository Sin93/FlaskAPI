# FlaskAPI
Задача:
Написать REST API по работе с сущностью User.

REST API должно удовлетворять следующие возможности:
• Добавление User
• Получение списка User
• Получение User по Id
• Редактирование User по Id
• Удаление User по Id

REST API должно работать с форматом данных JSON.

Сущность User должно состоять минимум из следующих полей:
• Идентификатор пользователя
• Отображаемое имя

В качестве хранилища данных нужно использовать файл в формате JSON.

Как с этим работать:
1. клонировать репозиторий на компьютер
2. установить библиотеки из файла requirements.txt
3. запустить файл app.py в интерпретаторе python, в шебанге прописан путь к стандартному интерпретатору на Linux
4. добавить несколько пользователей с помощью curl, запрос в bash:
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"NAME NEW USER", "age": 20}' http://localhost:5000/create_user
Имя "name" обязательно, а возраст "age" можно не указывать, тогда будет None. ID передавать не требуется, он генерируется автоматически на основе того, что было записано в id_counter
5. Вывести всех пользователей: curl http://localhost:5000/users
6. Вывести пользователя по ID: curl http://localhost:5000/users/{ID}
7. Изменить пользователя по ID:
curl -i -H "Content-Type: application/json" -X PUT -d '{"name":"Maxim", "age": 26}' http://localhost:5000/users/{ID}
Требуется передать имя пользователя "name" и/или возраст "age"
8. Удалить пользователя по ID: curl -X DELETE http://localhost:5000/users/{ID}
