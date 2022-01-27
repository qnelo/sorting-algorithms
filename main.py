from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.max_heap_arr import max_heap_sort as array_max_heap_sort
from sorting_algorithms.max_heap_tree import max_heap_sort as tree_max_heap_sort
from tools.generate_large_array import random_array

large_array = random_array(array_length=7000, biggest_number=1000000000000000)


# heap sort using max heap with binary tree
_, tmhs_stats = tree_max_heap_sort(large_array[:])
tmhs_stats.print()

# bubble sort test
_, bs_stats = bubble_sort(large_array[:])
bs_stats.print()

# heap sort using array implementation
_, amhs_stats = array_max_heap_sort(large_array[:])
amhs_stats.print()
