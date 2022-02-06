import random


def outer_sum(a, b):
    def inner_sum():
        nonlocal a
        nonlocal b
        return a + b
    return inner_sum() + 5


num_1 = random.randint(0, 10)
num_2 = random.randint(0, 10)

print(f"{num_1} + {num_2} + 5 = {outer_sum(num_1, num_2)}")
