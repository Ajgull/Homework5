# Домашнее задание 6

Исходные данные

![Исходные данные.png](Screenshots%2Ffilters%2F%D0%98%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5.png)

![first_filter.png](Screenshots%2Ffilters%2Ffirst_filter.png)

Проверка на несуществующий товар

![no_such_produce.png](Screenshots%2Ffilters%2Fno_such_produce.png)

Фильтр по цене

![фильтр по цене.png](Screenshots%2Ffilters%2F%D1%84%D0%B8%D0%BB%D1%8C%D1%82%D1%80%20%D0%BF%D0%BE%20%D1%86%D0%B5%D0%BD%D0%B5.png)

Поиск по части названия товара

![icontains.png](Screenshots%2Ffilters%2Ficontains.png)

Поиск по части отзыва о товаре

![Комментарий.png](Screenshots%2Ffilters%2F%D0%9A%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D0%B8%D0%B9.png)

![комментарии в admin.png](Screenshots%2Ffilters%2F%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D0%B8%D0%B8%20%D0%B2%20admin.png)

Поиск по части отзыва и части названи
![Название и комментраий.png](Screenshots%2Ffilters%2F%D0%9D%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%B8%D0%B9.png)

BooleanFilter по заказанным товарам

![Фильтр по заказанным товарам.png](Screenshots%2Ffilters%2F%D0%A4%D0%B8%D0%BB%D1%8C%D1%82%D1%80%20%D0%BF%D0%BE%20%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%D0%BC.png)

![Заказанные товары.png](Screenshots%2Ffilters%2F%D0%97%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B.png)

Поиск по названию и отзыву через Q запрос

![Поиск по названию и отзыву через Q запрос.png](Screenshots%2Ffilters%2F%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%BF%D0%BE%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E%20%D0%B8%20%D0%BE%D1%82%D0%B7%D1%8B%D0%B2%D1%83%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20Q%20%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81.png)

![Обновленный перечень отзывов.png](Screenshots%2Ffilters%2F%D0%9E%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%BF%D0%B5%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%8C%20%D0%BE%D1%82%D0%B7%D1%8B%D0%B2%D0%BE%D0%B2.png)








# Домашнее задание 4

## Задание 1

1 Создайте модель с базовыми полями и заполните базовой информацией.
Используйте ORM для создания объекта вашей модели(3 раза) и выполните
запрос в базу данных для получения всех записей(3 раза)/

![1_ex_add_models.png](Screenshots%2F1_ex_add_models.png)

![1_ex_add_new_models.png](Screenshots%2F1_ex_add_new_models.png)

![1_ex_request.png](Screenshots%2F1_ex_request.png)

![1_ex_request1.png](Screenshots%2F1_ex_request1.png)

![1_ex_request2.png](Screenshots%2F1_ex_request2.png)


## Задание 2

2 Используйте методы filter()(3 раза), exclude()(3 раза), и order_by()(3 раза).
Попробуйте создавать сложные запросы, а также сортироваться в определенном
порядке (по возрастанию или убыванию) а также фильтровать с разными
условиями (больше, меньше и тд)

filter():
![2_ex_filter().png](Screenshots%2F2_ex_filter%28%29.png)

![2_ex_filter()_exclude().png](Screenshots%2F2_ex_filter%28%29_exclude%28%29.png)

exclude():
![2_ex_filter()_exclude()_order_by.png](Screenshots%2F2_ex_filter%28%29_exclude%28%29_order_by.png)

![2_ex_more_requests.png](Screenshots%2F2_ex_more_requests.png)

## Задание 3

3 Создайте несколько моделей, которые будут иметь связь между собой.
Выполните различные запросы используя в условиях связь(3 раза). Попробуйте
также использовать values()(3 раза) и values_list()(3 раза) для получения только
нужной информации

![3_ex_relation_levels.png](Screenshots%2F3_ex_relation_levels.png)

values()
![3_ex_value.png](Screenshots%2F3_ex_value.png)

values_list()
![3_ex_values_list.png](Screenshots%2F3_ex_values_list.png)

## Задание 4

4 Изучите и используйте Q объектов для сложных условий. Создайте запрос,
который будет использовать Q объекты для объединения нескольких условий,
например, фильтрацию по нескольким полям с использованием логических
операторов "AND"(3 раза), "OR"(3 раза). Попробуйте объединить условия так,
чтобы одно из условий исключало записи, а другое — фильтровало их(3 раза).

![4_ex_Q_and.png](Screenshots%2F4_ex_Q_and.png)

![4_ex_Q_Or.png](Screenshots%2F4_ex_Q_Or.png)

mix of Q requests

![4_ex_Q_Mix.png](Screenshots%2F4_ex_Q_Mix.png)


## Задание 5

annotate()

![5_ex_annotate.png](Screenshots%2F5_ex_annotate.png)

aggregate()

![5_ex_aggregate.png](Screenshots%2F5_ex_aggregate.png)