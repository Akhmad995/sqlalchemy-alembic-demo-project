# python --version
# pip uninstall libname - удаление библиоетки
# pip freeze > requirements.txt - Список установленных библиотек
# pip install -r requirements.txt - Установка библиотек из списка
# pip install -U pyinstaller - проект в exe
# pyinstaller --onefile first.py
# pip install flask - фреймворк фласк
# pip install flask-wtf - библиотека для обратки форм

# Смена линтера CTRL + SHIFT + p, выбрать mypy

# python -m venv venv - виртуальное окружение
# source venv/Scripts/activate - активация

# pip install flask-migrate - библиотека для миграций, является оберткой для Alembic
# export FLASK_APP= {имя главного файла}
# flask db init
# flask db migrate -m 'Расширил модель пользотеля'
# flask db upgrade

# flask --app alch_app run - запуск приложения


# pip install Flask-SQLAlchemy - установка orm SQLAlchemy

# pip install alembic
# alembic init migrations
# alembic revision --autogenerate -m 'Добавил новую колонку'
# alembic upgrade head - применить изменения
# alembic downpgrade -1 -  откатиться на 1 ветку назад

# pip install python-dotenv - работа с файлом настроек

# pip install flask-login - библиотека для атворизации

# pip install Flask-RESTful
# pip install SQLAlchemy-serializer

