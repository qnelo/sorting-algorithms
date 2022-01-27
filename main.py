from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.max_heap_arr import max_heap_sort as array_max_heap_sort
from sorting_algorithms.max_heap_tree import max_heap_sort as tree_max_heap_sort
from tools.generate_large_array import random_array

large_array = random_array(array_length=7000, biggest_number=1000000000000000)


# heap sort using max heap with binary tree
tree_max_heap_sort_result = tree_max_heap_sort(large_array[:])

# bubble sort test
bubble_result = bubble_sort(large_array[:])

# heap sort using array implementation
array_max_heap_sort_result = array_max_heap_sort(large_array[:])
