# vacancy_catalog_api
REST API for VacancyCatalog web application

# Содержание

1. [Описание задачи](#Описание-задачи)
1. [Запуск](#Запуск)
1. [Тестирование](#Тестирование)
1. [Нагрузочное тестирование](#Нагрузочное-тестирование)
1. [Документация](#Документация)

# Описание задачи

Клиент-серверное приложение для поиска вакансий

Перечень функциональных требований:

1. Регистрация
2. Вход в систему
3. Выход из системы
4. Просомтр списка вакансий по индустриям
5. Просмотр списка вакансий по компаниям
6. Поиск вакансий по фильтрам
7. Просмотр информации о конкретной вакансии
8. Отправить отклик на вакансию
9. Просмотр своих откликов

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

## nginx
* Запустить nginx
```
sudo nginx
```

* Перезагрузит конфигурацию
```
sudo nginx -s reload
```

* Остановить процессы nginx с ожиданием окончания обслуживания текущих запросов рабочими процессами
```
sudo nginx -s quit
```

# Тестирование

1. Unit-тесты
2. Интеграционные тесты
3. e2e-тест

* Запуск тестов
```
docker-compose run web ./manage.py test
```

* Тестирование с использованием Behavior-driven development (нужен selenium и chromedriver)
```
python manage.py behave
```

* Процент покрытия тестами
```
docker-compose run web coverage run --source=catalog manage.py test
docker-compose run web coverage report
```

| Name          | Statements    | Missing       | Coverage      |
| ------------- | ------------- | ------------- | ------------- |
|catalog/\_\_init\_\_.py|                                       0|      0|   100%|
|catalog/admin.py|                                          7|      0|   100%|
|catalog/apps.py|                                           4|      0|  100%|
|catalog/managers.py|                                      14|     11|    21%|
|catalog/models.py|                                        53|     10|    81%|
|catalog/serializers.py|                                   43|      1|    98%|
|catalog/tests/\_\_init\_\_.py|                                 0|      0|   100%|
|catalog/tests/e2e_test/\_\_init\_\_.py|                        0|      0|   100%|
|catalog/tests/e2e_test/test_e2e.py|                       48|      0|   100%|
|catalog/tests/integration_tests/\_\_init\_\_.py|               0|      0|   100%|
|catalog/tests/integration_tests/test_integration.py|      57|      3|    95%|
|catalog/tests/unit_tests/\_\_init\_\_.py|                      0|      0|   100%|
|catalog/tests/unit_tests/test_models.py|                 113|      0|   100%|
|catalog/tests/unit_tests/test_serializers.py|            106|      0|   100%|
|catalog/tests/unit_tests/user_builder.py|                 12|      2|    83%|
|catalog/urls.py|                                          10|      0|   100%|
|catalog/views.py|                                         30|      0|   100%|
Total                                          |         504 |    27 |   95% |


# Нагрузочное тестирование

Нагрузочное тестирование проведено для 1000 запросов с помощью утилиты Apache Benchmark. Результаты представлены в файле [ab_results.md](./ab_results.md)


# Документация

Документация в формате Swagger находится по адресу: http://127.0.0.1:8000/api/

## Use-case диаграмма системы

![Usecase](https://github.com/oljakon/vacancy_catalog_api/blob/master/docs/usecase.png)


## ER-диаграмма сущностей системы

![ER](https://github.com/oljakon/vacancy_catalog_api/blob/master/docs/er.png)

## Диаграмма базы данных

![DB](https://github.com/oljakon/vacancy_catalog_api/blob/master/docs/database.png)
