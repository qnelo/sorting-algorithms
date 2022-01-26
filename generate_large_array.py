import random


def generate_random_array(array_length: int, biggest_number: int) -> None:
    arr = []
    for _ in range(array_length):
        arr.append(random.randrange(0, biggest_number, 1))

    file = open("large_array.py", "w")
    file.write(f"large_array = {str(arr)}")
    file.close()


generate_random_array(array_length=7000, biggest_number=1000000000000000)
