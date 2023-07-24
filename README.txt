# Backend for project management system

It is necessary to write a REST API that provides functionality for
project management, tasking, etc.

-- API Methods
- Users:
	- User Registration 
	- User Authorization 
- Projects:
	- Project Creation 
	- Getting the list of projects 
- Tasks:
	- Entering a task within a project 
	- Search for tasks with filtering by fields
	- Retrieving a task 
	- Adding a comment to a task 
	- Changing task status

-- Models --
Project Model:
	- Project Name

User Model:
	- username
	- password

Task Model:
	- Task name
	- Task description
	- task status
	- project within which the task is created
	- task creation date
	- task closing date
	- User who started the task
	- User who started the task
	- list of files - (file uploading is done, displaying in the database is not done )
	- comment list

Comment model:
	- Text
	- Comment Author

-- Requirements for the project --
	- passwords must be stored in the database in encrypted form 
	- only registered users can access methods in "Projects" and "Tasks" sections.
	- DB - Postgres (connected online via ElephantSql.com)
	- project should be deployed in docker (tap1x/testtask:image)

Libraries used:
- flask
- marshmallow
- sqlalchemy


_______________________________________________________________________________


Бэкенд для системы менеджмента проектов

Необходимо написать REST API, предоставляющий функционал для
управления проектами, заведения задач и т.д.

-- Методы API --
- Пользователи:
	- Регистрация пользователя 
	- Авторизация пользователя 
- Проекты:
	- Создание проекта 
	- Получение списка проектов 
- Задачи:
	- Заведение задачи в рамках проекта 
	- Поиск задач с фильтрацией по полям
	- Получение задачи 
	- Добавление комментария к задаче 
	- Изменения статуса задачи

-- Модели --
Модель Проекта:
	- Название проекта

Модель пользователя:
	- юзернейм
	- пароль

Модель задачи:
	- Название задачи
	- Описание задачи
	- статус задачи
	- проект, в рамках которого заведена задача
	- дата заведения задачи
	- дата закрытия задачи
	- Пользователь, который завел задачу
	- Пользователь, на которого завели задач
	- список файлов - (загрузку файлов сделал, отображение в бд не сделал )
	- список комментариев

Модель комментария:
	- Текст
	- Автор комментария

-- Требования к проекту --
	- пароли должны храниться в базе в зашифрованном виде 
	- обращаться к методам в разделах "Проекты" и "Задачи" могут только зарегистрированные пользователи
	- БД - Postgres (подключил онлайн через ElephantSql.com)
	- проект должен разворачиваться в докере (tap1x/testtask:image)

Используемые библиотеки:
- flask
- marshmallow
- sqlalchemy
