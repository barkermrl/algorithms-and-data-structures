"""An implementation of a priority queue with a (binary) max-heap.

Heaps were originally introduced in 1964 by J. W. J. Williams in the context of
the Heapsort algorithm.

Reference:
- J. Williams, "Algorithm 232 – Heapsort", Communications of the ACM (1964)

The code draws inspiration from descriptions of Priority Queues and Binary Heaps:
- Chapter 8 of Elementary Algorithms by Liu Xinyu https://github.com/liuxinyu95/AlgoXY
- Chapter 6 of T. H. Cormen, et al., "Introduction to algorithms", MIT press (2022)

Note: this implementation assumes all keys are unique.

If you would like to read a "production quality" version of a priority queue you
may find the cpython implementation interesting:
https://github.com/python/cpython/blob/3.11/Lib/heapq.py
"""

from red_black_tree import RedBlackTree


def left_child(i: int) -> int:
    """Compute the index of the left child of node i.

    Args:
        i: the index of the node.

    Returns:
        The index of the left child of node i.
    """
    raise NotImplementedError


def right_child(i: int) -> int:
    """Compute the index of the right child of node i.

    Args:
        i: the index of the node.

    Returns:
        The index of the right child of node i.
    """
    raise NotImplementedError


def parent(i: int) -> int:
    """Compute the index of the parent of node i.

    Args:
        i: the index of the node.

    Returns:
        The index of the parent of node i.
    """
    raise NotImplementedError


def max_heapify(A: list, heap_size: int, i: int):
    raise NotImplementedError


def build_max_heap(A):
    raise NotImplementedError


class MaxPriorityQueue:

    def __init__(self, A: list):
        self.A = A
        self.heap_size = len(A)

        # we use a red-black tree to map values to indices in the underlying array
        # so that we can call increase_key in O(log n) time
        self.value2index = RedBlackTree()

    def get_maximum(self):
        """Return the maximum value in the priority queue.

        Returns:
            The maximum value in the priority queue.
        """
        raise NotImplementedError

    def pop_max(self):
        """Remove the maximum value from the priority queue.

        Returns:
            The maximum value in the priority queue.
        """
        raise NotImplementedError

    def increase_key(self, key, value):
        """Increase the key of the value in the priority queue.

        Args:
            key: the new key of the value
            value: the value to increase the key of
        """
        raise NotImplementedError

    def insert(self, key, value):
        """Insert value with given key into the priority queue

        Args:
            key: the key of the value to insert
            value: the value to insert
        """
        raise NotImplementedError

    def __repr__(self):
        summary = "\n".join(str(x) for x in self.A[:self.heap_size])
        return f"MaxPriorityQueue containing:\n{summary}"


def main():
    # pylint: disable=line-too-long
    # flake8: noqa: E501

    inital_queue = []
    max_priority_queue = MaxPriorityQueue(A=inital_queue)
    print("Initial priority queue:")
    print(max_priority_queue)

    max_priority_queue.insert(key=3, value="green")
    max_priority_queue.insert(key=2, value="yellow")
    max_priority_queue.insert(key=4, value="blue")
    max_priority_queue.insert(key=-1, value="mauve")
    print("\nPriority queue after insertions:")
    print(max_priority_queue)

    max_priority_queue.increase_key(key=5, value="green")
    print("\nPriority queue after key increase:")
    print(max_priority_queue)

    print(f"\nPopped max:", max_priority_queue.pop_max())
    print(f"Popped max:", max_priority_queue.pop_max())
    print("\nPriority queue after pop max calls:")
    print(max_priority_queue)

    """
    Print out >>>

    Initial priority queue:
    MaxPriorityQueue containing:
    {'key': 0, 'value': 'red'}

    Priority queue after insertions:
    MaxPriorityQueue containing:
    {'key': 4, 'value': 'blue'}
    {'key': 2, 'value': 'yellow'}
    {'key': 3, 'value': 'green'}
    {'key': -1, 'value': 'mauve'}

    Priority queue after key increase:
    MaxPriorityQueue containing:
    {'key': 5, 'value': 'green'}
    {'key': 2, 'value': 'yellow'}
    {'key': 4, 'value': 'blue'}
    {'key': -1, 'value': 'mauve'}

    Popped max: green
    Popped max: blue

    Priority queue after pop max calls:
    MaxPriorityQueue containing:
    {'key': 2, 'value': 'yellow'}
    {'key': -1, 'value': 'mauve'}
    """

if __name__ == "__main__":
    main()
