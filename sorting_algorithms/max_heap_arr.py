from tools.decorators import statistics


def __parent_order(arr: list, index: int):

    while index > 0:
        parent_index = (index - 1) // 2
        if arr[parent_index] < arr[index]:
            arr[parent_index], arr[index] = arr[index], arr[parent_index]
        index = parent_index


def __max_heap_generator(arr: list, arr_len: int) -> list:

    for n in range(arr_len // 2):
        left = (n * 2) + 1
        right = (n * 2) + 2

        if right < arr_len:
            if arr[n] < arr[left] < arr[right]:
                arr[n], arr[right] = arr[right], arr[n]
            if arr[n] < arr[right] < arr[left]:
                arr[n], arr[left] = arr[left], arr[n]
            __parent_order(arr=arr, index=right)
        else:
            if arr[n] < arr[left]:
                arr[n], arr[left] = arr[left], arr[n]
        __parent_order(arr=arr, index=left)

    return arr


@statistics
def max_heap_sort(arr: list) -> list:

    arr_len = len(arr)
    __max_heap_generator(arr=arr, arr_len=arr_len)

    for n in range(arr_len - 1):
        last_position = arr_len - 1 - n
        arr[0], arr[last_position] = arr[last_position], arr[0]
        __max_heap_generator(arr=arr, arr_len=last_position)

    return arr
