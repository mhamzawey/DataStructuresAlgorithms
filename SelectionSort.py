def selectionSort(arr):
    """
    The selection sort algorithm sorts an array by repeatedly
     finding the minimum element from unsorted part and putting
      it at the beginning.
      The algorithm maintains two subarrays in a given array.
    :param arr:
    :return: arr
    Complexity O(n^2)
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp

    return arr


o_array = [54, 26, 93, 17, 77, 31, 44, 55, 20,89,0]
print("Selection Sort Algorithm: " + str(selectionSort(o_array)))
