from tools.decorators import statistics


class MaxHeap:
    def __init__(self, value: int, index: int) -> None:
        self.left = None
        self.right = None
        self.value = value
        self.index = index

    def __get_node(self, node_index: int) -> "MaxHeap":
        binary_path = bin(node_index).replace("0b", "")
        node = self
        for path in binary_path[1:]:
            if path == "0":
                node = node.left
            else:
                node = node.right
        return node

    def __parent_order(self, root: "MaxHeap", index: int) -> None:

        if index == 1:
            return

        node_to_compare = root.__get_node(index // 2)

        if node_to_compare.value < self.value:
            node_to_compare.value, self.value = self.value, node_to_compare.value

        node_to_compare.__parent_order(root, node_to_compare.index)

    def max_heap_insert(
        self, node_index: int, left_value: int = None, right_value: int = None
    ) -> None:

        node = self.__get_node(node_index=node_index)
        node.left = (
            MaxHeap(value=left_value, index=node_index * 2)
            if left_value is not None
            else None
        )
        node.right = (
            MaxHeap(value=right_value, index=(node_index * 2) + 1)
            if right_value is not None
            else None
        )

        node.left.__parent_order(root=self, index=node.left.index)
        if node.right:
            node.right.__parent_order(root=self, index=node.right.index)

    def __heapify(self):
        if self.right:
            if self.left.value < self.right.value:
                if self.value < self.right.value:
                    self.value, self.right.value = self.right.value, self.value
                    self.right.__heapify()
                    return
        if self.left:
            if self.value < self.left.value:
                self.value, self.left.value = self.left.value, self.value
                self.left.__heapify()

    def heap_sort(self, arr_len: list) -> list:

        ordered_array = []

        for _ in range(1, arr_len):

            # Insert in the list the value of the tree root
            # which is the highest value of the structure
            ordered_array.insert(0, self.value)

            # Put the value of the last node in the root of the tree
            last_node = self.__get_node(arr_len)
            self.value = last_node.value

            # Delete the last node whose value was put in the root of the tree
            last_node_parent = self.__get_node(arr_len // 2)
            if (arr_len % 2) == 0:
                last_node_parent.left = None
            else:
                last_node_parent.right = None

            # Order the tree to comply with max heap rules
            self.__heapify()
            arr_len -= 1

        return ordered_array


def __max_heap_generator(arr: list) -> MaxHeap:

    index = 0
    arr_len = len(arr)

    cbt = MaxHeap(arr[0], index=1)

    for n in range(1, arr_len, 2):
        right = arr[n + 1] if n + 1 < arr_len else None
        index += 1
        cbt.max_heap_insert(node_index=index, left_value=arr[n], right_value=right)

    return cbt


@statistics
def max_heap_sort(arr: list) -> list:
    max_heap_tree = __max_heap_generator(arr=arr)
    ordered_array = max_heap_tree.heap_sort(arr_len=len(arr))
    return ordered_array
