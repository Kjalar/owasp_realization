Broken access control case

Имеющиеся данные:
username: tommy
password: tommysuper

Необходимо найти флаг пользователя admin


Запуск:
# установите виртуальное окружение
python3 -m venv venv

# включите виртуальное окружение
source ./venv/bin/activate

# установите необходимые пакеты
pip install -r ./requirements.txt

# запустите сервер
python manage.py runserver

# перейдите по ссылке
http://127.0.0.1:8000/login/

Решение:
http://127.0.0.1:8000/account/265