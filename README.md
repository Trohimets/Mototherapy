Ознакомиться с проектом можно по адресу https://motoemotion.ru/


# Описание проекта Mototherapy

"Сайт объединения MotoEmotion — сообщества людей, связанных общими интересами — мотоциклы и большие добрые сердца.

Мы прововодим праздники для детей с ограниченными возможностями и помогаем детским центрам.

Исполнение мечт — наш конёк."

# Используемые технологии

Python, Django, Django ORM, Django REST Framework (DRF), REST API, Postgres

## Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Trohimets/mototherapy.git
```
```
cd mototherapy
```
- Cоздать и активировать виртуальное окружение:
```
py -m venv venv
```
```
source venv/scripts/activate
```
- Установить менджером pip в проект Poetry:
```
pip install poetry
```
- Установить зависимости проекта:
```
poetry isntall
```
- Выполнить миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
```

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
