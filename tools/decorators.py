import time
import tracemalloc


def __verifier(arr: int) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def statistics(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        tracemalloc.start()

        arr = func(*args, **kwargs)
        current_size, peak_size = tracemalloc.get_traced_memory()

        tracemalloc.stop()
        total_time = time.time() - start_time

        print(
            f"With \"{func.__name__}\" - order time:{total_time}, memory used:{current_size}, peak memory used:{peak_size}"
        )

        valid = __verifier(arr=arr)
        if not valid:
            print("List not sorted correctly")

        stats = {
            "total_time": total_time,
            "used_size_memory": current_size,
            "peak_size_memory": peak_size,
        }
        return arr, stats

    return wrapper
