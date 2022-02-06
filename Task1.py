import random


def calculations(a, b):
    return a + b, a - b


num_1 = random.randint(0, 100)
num_2 = random.randint(0, 100)


sum, sub = calculations(num_1, num_2)


print(f"{num_1} + {num_2} = {sum}\n{num_1} - {num_2} = {sub} ")
