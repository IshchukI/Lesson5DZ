import random

RANDOM_UPPER_BOUND = 10
LIST_SIZE = 5

data_list = list()


def random_list_generation(LIST_SIZE, RANDOM_UPPER_BOUND):
    for _ in range(0, LIST_SIZE):
        data_list.append(random.randint(0, RANDOM_UPPER_BOUND))


def multiple_el_of_list(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] * multiple_el_of_list(list[1:])


random_list_generation(LIST_SIZE, RANDOM_UPPER_BOUND)
print(f"произведение элементов списка {data_list} равно: {multiple_el_of_list(data_list)}")
