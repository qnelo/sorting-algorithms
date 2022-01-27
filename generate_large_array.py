import random


def random_array(array_length: int, biggest_number: int) -> list:
    arr = []
    for _ in range(array_length):
        arr.append(random.randrange(0, biggest_number, 1))

    return arr
