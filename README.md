# To-Do List Web Application

## Описание проекта

Приложение поддерживает функционал регистрации, авторизации, добавления, редактирования, удаления задач, а также позволяет помечать задачи как выполненные. Есть возможность фильтрации задач по статусу и сортировки по дате создания и статусу.

## Технический стек

- **Backend**: Django, Django REST Framework (DRF), PostgreSQL
- **Frontend**: React, Axios для взаимодействия с API
- **База данных**: PostgreSQL
- **Аутентификация**: JWT (JSON Web Token)
- **Тесты**: Тестирование основных функций API

## Установка и запуск

### 1. Backend (Django)

#### Установка зависимостей

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app

2. Установите зависимости:
    pip install -r requirements.txt

## Настройка базы данных

1. Убедитесь, что PostgreSQL установлен и запущен.

2. Создайте базу данных PostgreSQL:
    CREATE DATABASE tododb;
    CREATE USER postgres WITH PASSWORD 'your_password';
    GRANT ALL PRIVILEGES ON DATABASE todo_db TO todo_user;

3. Обновите настройки базы данных в settings.py:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tododb',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

4. Примените миграции:
    python manage.py migrate

## Запуск серверной части

1. Создайте суперпользователя (для доступа к админке Django):
    python manage.py createsuperuser

2. Запустите сервер разработки:
    python manage.py runserver

API будет доступен по адресу http://127.0.0.1:8000.

# 2. Frontend (React)
Установка зависимостей
1. Перейдите в директорию фронтенда:
    cd frontend
2. Установите зависимости:
    npm install

## Запуск фронтенда
Запустите React-приложение:
    npm start

# 3. Тестирование
Тестирование API
Запуск юнит-тестов для серверной части:
    python manage.py test
