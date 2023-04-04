"""A simple implementation of the radix sort (least significant digit) algorithm.

Radix sort is a "folk" algorithm, i.e. it is not based on a specific paper, that
incorporates several ideas. Typically it uses counting sort as a subroutine (as
we do here), but other stable sorting algorithms can be used as well.

This code is based on the description of the algorithm in the following sources:
- https://en.wikipedia.org/wiki/Radix_sort
- Chapter 8 of T. H. Cormen, et al., "Introduction to algorithms", MIT press (2022)

Notes:
- for simplicity, the code does not focus on efficiency (it is wasteful with memory)
- it also assumes that the keys are integers
"""


def counting_sort_on_digit(A, k, d, digit_pos):
    """Sort the given array with the counting sort algorithm on the given digit.

    Args:
        A: the array to be sorted.
        k: the number of possible values for the keys (assumes k <= 10).
        d: the number of digits in the keys.
        digit_pos: the position of the digit to sort on

    Returns:
        The sorted array.

    NOTE: Counting sort assumes that all inputs are tuples of integers between
    0 and k-1 inclusive.
    """

    assert k <= 10, "This implementation of counting sort assumes k <= 10."

    def subkey(key):
        """Helper function to extract the digit at the given position from the key."""
        raise NotImplementedError

    raise NotImplementedError


def radix_sort_lsd(A, d, k):
    """Sort the given array with the radix sort algorithm using a
    least significant digit (LSD) ordering.

    Args:
        A: the array to be sorted.
        d: the number of digits in the keys.
        k: the number of possible digit values

    Returns:
        The sorted array.
    """
    raise NotImplementedError


def main():
    A = [314, 712, 632, 201, 111]
    # the number of digits in each key
    d = 3
    k = 10
    print("Array to be sorted:")
    print(A)
    B = radix_sort_lsd(A, d=d, k=k)
    print("Array sorted with radix sort (LSD):")
    print(B)

    """
    Print out >>>

    Array to be sorted:
    [314, 712, 612, 201, 111]
    Array sorted with radix sort (LSD):
    [111, 201, 314, 612, 712]
    """


if __name__ == "__main__":
    main()