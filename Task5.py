import random

RANDOM_UPPER_BOUND = 10000
LIST_SIZE = 5

data_list = list()


def random_list_generation(LIST_SIZE, RANDOM_UPPER_BOUND):
    for _ in range(0, LIST_SIZE):
        data_list.append(random.randint(0, RANDOM_UPPER_BOUND))


def sum_of_numbers(num):
    if num < 10:
        return num
    else:
        return num % 10 + sum_of_numbers(num // 10)


random_list_generation(LIST_SIZE, RANDOM_UPPER_BOUND)
for el in data_list:
    print(f"сумма цифр {el} = {sum_of_numbers(el)}")
