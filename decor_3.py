import os
from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        start_time = datetime.now()
        result = old_function(*args, **kwargs)
        my_text = f'{start_time}, {old_function.__name__}, {args}, {kwargs}, {result}\n'
        with open("main.log", "a") as my_file:
            my_file.write(my_text)
        return result
    return new_function


@logger
def flat_generator(list_of_lists):

    for i in list_of_lists:
        for j in i:
            yield j


def test_3():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for item in flat_generator(list_of_lists_1):
        print(item)


if __name__ == '__main__':
    test_3()
