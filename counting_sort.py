"""A simple implementation of the counting sort algorithm.

Counting sort was originally described by H. Seward in 1959 in his Master's thesis under
the name "Floating Digital Sort".

Reference:
- H. Seward, "Information sorting in the application of electronic digital computers to
business operations", Dissertation MIT (1954)

This code is based on the description of the algorithm in the following sources:
- https://en.wikipedia.org/wiki/Counting_sort
- Chapter 8 of T. H. Cormen, et al., "Introduction to algorithms", MIT press (2022)
"""


def counting_sort(A, k):
    """Sort the given array with the counting sort algorithm.

    Args:
        A: the array to be sorted.
        k: the number of possible values for the keys.

    Returns:
        The sorted array.

    NOTE: Counting sort assumes that all inputs are integers between 0 and k-1 inclusive.
    """
    raise NotImplementedError


def main():
    A = [3, 1, 4, 0, 0, 3]
    # the number of possible keys (which range from 0 to k - 1)
    k = 5
    print("Array to be sorted:")
    print(A)
    B = counting_sort(A, k=k)
    print("Array sorted with counting sort:")
    print(B)

    """
    Print out >>>

    Array to be sorted:
    [3, 1, 4, 0, 0, 3]
    Array sorted with counting sort:
    [0, 0, 1, 3, 3, 4]
    """


if __name__ == "__main__":
    main()
