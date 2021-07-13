Broken access control case

Имеющиеся данные:
список пользователей по запросу GET (10 пользователей)
localhost:8000/user

удаление пользователя по запросу POST
localhost:8000/user/user2
удалит пользователя user2

возращаемые ответы на запросы POST
удалить несуществующего юзера - 400
удалить юзера - 204


Запуск:
# перейдите в директорию с файлом requirements.txt
# установите виртуальное окружение
python3 -m venv venv

# включите виртуальное окружение
source ./venv/bin/activate
(или .\venv\Scripts\activate.bat)

# установите необходимые пакеты в виртуальное окружение
pip install -r ./requirements.txt
(или pip install -r .\requirements.txt)

# запустите сервер, перейдя в папку с файлом manage.py
python manage.py runserver
