def bubble_sort(x: list[float]) -> None:
    """Sorts a list of floating-point numbers using the bubble sort algorithm.

    Args:
        x: The list of numbers to be sorted.

    Returns:
        None. The list `x` is sorted in-place.
    """

    for i in range(len(x)):
        for j in range(len(x) - 1 - i):
            if x[j] > x[j + 1]:
                temp = x[j + 1]
                swap = False
                x[j + 1] = x[j]
                x[j] = temp
            if not swap:
                break


a = [1, 3, 2, 4, 5]
bubble_sort(a)
print(a)
