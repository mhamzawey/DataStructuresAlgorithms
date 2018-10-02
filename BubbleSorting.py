def bubbleSort(arr):
    """
    Bubble Sort is the simplest sorting algorithm that
    works by repeatedly swapping the adjacent elements
    if they are in wrong order.
    Complity: O(n^2)
    :param arr:
    :return: arr
    """
    array = arr
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return array


test_array = [54, 26, 93, 17, 77, 31, 44, 55, 20,89,0,87]
print("Bubble Sort Algorithm: " + str(bubbleSort(test_array)))
