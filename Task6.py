import random

def fibonachi(value):
    if value <= 0:
        return 0
    elif value == 1:
        return 1
    else:
        return fibonachi(value - 1) + fibonachi(value - 2)

val = random.randint(0,15)
print(f"{val} число ряда Фибоначи: {fibonachi(val)}")