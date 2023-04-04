"""A simple implementation of the bucket sort algorithm.

Bucket sort is a distribution algorithm that involves three steps:
1. Scatter - distribute keys to buckets
2. Sort - sort keys within each bucket
3. Gather - gather the sorted keys in order

This code is based on the description of the algorithm in the following sources:
- https://en.wikipedia.org/wiki/bucket_sort
- Chapter 8 of T. H. Cormen, et al., "Introduction to algorithms", MIT press (2022)
"""


def bucket_sort(A: list):
    """Sort the given input A using bucket sort.

    Args:
        A: the array to be sorted.

    Returns:
        The sorted array.
    """
    raise NotImplementedError


def insertion_sort(A: list):
    """Sort the given input A using insertion sort.

    Args:
        A: the array to be sorted.

    Returns:
        The sorted array.
    """
    raise NotImplementedError


def main():
    A = [0.15, 0.4, 0.18, 0.8, 0.13]
    # the number of digits in each key
    print("Array to be sorted:")
    print(A)
    A = bucket_sort(A)
    print("Array sorted with bucket sort:")
    print(A)

    """
    Print out >>>

    Array to be sorted:
    [0.15, 0.4, 0.18, 0.8, 0.13]
    Array sorted with bucket sort:
    [0.13, 0.15, 0.18, 0.4, 0.8]
    """


if __name__ == "__main__":
    main()
