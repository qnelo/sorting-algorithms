const { randomArray } = require("./tools/generate_large_array")
const { maxHeapSort } = require("./sorting_algorithms/max_heap_arr")

const largeArray = randomArray(5000, 1000000000000000)
// const largeArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

const { statistics } = maxHeapSort(largeArray)
statistics.print()
