from large_array import large_array
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.max_heap import max_heap_sort as tree_mh_sort
from sorting_algorithms.max_heap_arr import max_heap_sort as array_mh_sort

# heap sort using max heap with binary tree
tree_mh_sort_result = tree_mh_sort(large_array[:])

# bubble sort test
bubble_result = bubble_sort(large_array[:])

# heap sort using array implementation
array_mh_sort_result = array_mh_sort(large_array[:])
