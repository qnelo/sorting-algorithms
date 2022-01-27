from tools.decorators import statistics


@statistics
def bubble_sort(arr: list) -> list:
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(len_arr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
