def funk(*args):
    for i in range(0, len(args)):
        print(f"args[{i}] = {args[i]}")


funk(1, 22, "asd", "sd", "a", 33.33)
