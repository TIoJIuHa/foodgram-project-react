# Foodgram — продуктовый помощник

Сервис позволяет размещать рецепты различных блюд.
Здесь вы можете:
- Создавать или редактировать свои рецепты
- Изучать рецепты других пользователей, добавлять их в избранное или в корзину
- Подписываться на пользователей и узнавать об обновлениях
- Скачать список ингредиентов из корзины, необходимых для приготовления блюд

## Локальный запуск
Для локального запуска необходимо выполнить следующие шаги:

- Клонируйте репозиторий:
```
git clone git@github.com:TIoJIuHa/foodgram-project-react.git
```
- Запустите docker и docker-compose:
```
cd infra
docker-compose up -d
```
- Выполните миграции в контейнере:
```
docker-compose exec foodgram_backend python manage.py migrate
```
- Собрите статику в контейнере:
```
docker-compose exec foodgram_backend python manage.py collectstatic --noinput
```
- Создайте суперпользователя Django 
```
sudo docker-compose exec backend python manage.py createsuperuser
```
- Заполните БД подготовленными данными при первом запуске
```
sudo docker-compose cp ../data/ingredients.json backend:/app/ingredients.json 
```
```
sudo docker-compose exec backend python manage.py import_ingredients ingredients.json
```
Проект будет запущен на локальном хосте http://localhost/

## Запуск на сервере
Если вы хотите развернуть этот проект на удаленном хосте, нужно выполнить следующие шаги:
- Убедитесь, что у вас уже установлен docker и docker-compose
- Склонируйте репозиторий
```
git clone git@github.com:TIoJIuHa/foodgram-project-react.git
```
- Поменяйте настройки в infra/nginx.conf: напишите свой IP
* Склонируйт файлы nginx.conf и docker-compose.yaml на сервер
```
scp nginx.conf <username>@<server>:/etc/nginx/conf.d/default.conf
```
```
scp docker-compose.yaml <username>@<server>:/home/<username>/docker-compose.yaml
```
- Создайте .env файл
Пример:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=user
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS = http://localhost,http://localhost:8000,http://127.0.0.1:8000
```
- Перейдите в директорию с файлом docker-compose
```
sudo docker-compose up -d
```
- Не забудьте выполнить миграции и собрать статику

Сервис доступен по вашему адресу.
