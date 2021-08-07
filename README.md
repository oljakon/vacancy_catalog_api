# vacancy_catalog_api
REST API for VacancyCatalog web application

# Содержание

1. [Запуск](#Запуск)
1. [Тестирование](#Тестирование)


# Запуск

* Клонировать проект с репозитория GitHub
```
git clone https://github.com/oljakon/vacancy_catalog_api.git
```

* Перейти в директорию *vacancy_catalog_ap*
```
cd vacancy_catalog_ap/
```

* Запустить *docker_compose*
```
docker-compose up
```

# Тестирование

* Запуск тестов
```
docker-compose run web ./manage.py test
```
