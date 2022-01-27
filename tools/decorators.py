import sys
import time
import tracemalloc
from types import FunctionType


class Statistics:
    def __init__(self, stats: dict) -> None:
        self.stats = stats

    def print(self) -> None:
        BOLD, YELLOW, RED, NORMAL = "\033[1m", "\033[93m", "\033[91m", "\033[0m"

        inconsistent_message = (
            f"{YELLOW} ⚠ WARNING: inconsistent length{NORMAL}"
            if self.stats.get("arr_len") != self.stats.get("arr_result_len")
            else ""
        )
        valid_sort_message = f"List{'' if self.stats.get('valid_sort') else f' {RED}NOT{NORMAL}'} sorted correctly"

        print(
            f"""'{BOLD}{self.stats.get("function_name")}{NORMAL}' statistics
            {valid_sort_message}
            array size: {self.stats.get("arr_size")} - array result size: {self.stats.get("arr_result_size")}
            array length: {self.stats.get("arr_len")} - result array length: {self.stats.get("arr_result_len")}{inconsistent_message}
            order time: {self.stats.get("total_time")}
            memory used: {self.stats.get("used_size_memory")}KiB, peak memory used: {self.stats.get("peak_size_memory")}KiB"""
        )


def __verifier(arr: int) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def statistics(func: FunctionType) -> FunctionType:
    def wrapper(*args, **kwargs) -> tuple:

        start_time = time.time()
        tracemalloc.start()

        arr_result = func(*args, **kwargs)
        used_size_memory, peak_size_memory = tracemalloc.get_traced_memory()

        tracemalloc.stop()
        total_time = time.time() - start_time

        stats = {
            "function_name": func.__name__,
            "arr_len": len(args[0]),
            "arr_size": sys.getsizeof(args[0]),
            "arr_result_len": len(arr_result),
            "arr_result_size": sys.getsizeof(arr_result),
            "valid_sort": __verifier(arr=arr_result),
            "total_time": total_time,
            "used_size_memory": used_size_memory,
            "peak_size_memory": peak_size_memory,
        }

        return arr_result, Statistics(stats=stats)

    return wrapper
