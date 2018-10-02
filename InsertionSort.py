from BinarySearch import binarySearch


def insertionSort(arr):
    """
    Insertion sort is a simple sorting algorithm
    that works the way we sort playing cards in our hands.
    :param arr:
    :return: arr
    Complexity O(n^2
    """
    for i in range(len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = current
    return arr


x_array = [54, 26, 93, 17, 77, 31, 44, 55, 20, 89, 0]
print("Insertion Sort Algorithm: " + str(insertionSort(x_array)))
y = binarySearch(55, x_array, 0, len(x_array) - 1)
print(y)

