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