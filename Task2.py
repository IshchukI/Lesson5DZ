import random

RANDOM_UPPER_BOUND = 100
LIST_SIZE = 5

data_list = list()


def random_list_generation(LIST_SIZE, RANDOM_UPPER_BOUND):
    random_list = list()
    for _ in range(0, LIST_SIZE):
        random_list.append(random.randint(0, RANDOM_UPPER_BOUND))
    return random_list


def sum_of_list_element():
    sum = 0
    for element in data_list:
        sum += element
    return sum


data_list = random_list_generation(LIST_SIZE, RANDOM_UPPER_BOUND)
sum_of_list_el = sum_of_list_element()

print(f"сумма всех элементов списка {data_list} = {sum_of_list_el}")
