# MelonTime

[Демо](https://knaubdev.pythonanywhere.com/) [Демо 2](https://daniilknaub.fvds.ru)

## Описание

Web-приложение для планирования задач.
Функционал приложения состоит из:
1. Регистрация, авторизация и выход пользователя из системы;
2. Создание, завершение и удаление задач;
3. Просмотр текущих и завершенных задач.

## Cтек технологий
1. Python
2. Django
3. Bootstrap
4. Git VCS
5. SQLite3
6. DjangoTemplates

## Запуск приложения на локальном устройстве
Склонируйте репозиторий с помощью ```git clone https://github.com/DanielKnaub/melontime-project.git```.
Создайте виртуальное окружение командой ```python3 -m venv venv``` и активируйте его ```source venv/bin/activate```.

Установите необходимые зависимости ```pip install -r requirements.txt```, создайте файл .env  в директории melontime/ и укажите в нём следующие параметры 
```commandline
SECRET_KEY=YOUR_SECRET_KEY
ALLOWED_HOSTS=["*"]
DEBUG=False
```
Проведите миграцию в базу данных ```python3 manage.py migrate```
и запустите из корневой директории локальный сервер ```python3 manage.py runserver```.

## Перспективы развития
1. [x] Добавить push-уведомления;
2. [x] Добавить конечный срок выполнения задачи;
3. [x] Реализовать тёмную тему оформления клиентской части;
4. [x] Перевести приложение на английский язык.
