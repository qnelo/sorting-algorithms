from large_array import large_array
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.max_heap import max_heap_sort

# heap sort test
max_heap_result = max_heap_sort(large_array)

# bubble sort test
bubble_result = bubble_sort(large_array[:], len(large_array))
