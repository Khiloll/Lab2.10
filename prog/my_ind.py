#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Самостоятельно подберите или придумайте задачу с переменным числом именованных
# аргументов. Приведите решение этой задачи.

def my_func(**kwargs):
    """
    Вывод на экран аргументов, переданных в функцию, с их названиями
    """
    for key, value in kwargs.items():
        print("{0}: {1}".format(key, value))
    print()


if __name__ == "__main__":
    my_func(name="Хилол", age=21)
    my_func(city="Ставрополь", country="Россия")
    my_func(hobby="Баскетбол", job="Студент", salary=14000)
