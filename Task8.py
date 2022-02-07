import random

RANDOM_UPPER_BOUND = 10
LIST_SIZE = 10

data_list = list()


def random_list_generation(LIST_SIZE, RANDOM_UPPER_BOUND):
    for _ in range(0, LIST_SIZE):
        data_list.append(random.randint(0, RANDOM_UPPER_BOUND))


def is_two_squared(n):
    if (n / 2) >= 2:
        return is_two_squared(n / 2)
    else:
        if n == 2:
            return f"Yes"
        else:
            return "No"


random_list_generation(LIST_SIZE, RANDOM_UPPER_BOUND)
for el in data_list:
    print(f"Число {el} является степенью двойки: {is_two_squared(el)}")



