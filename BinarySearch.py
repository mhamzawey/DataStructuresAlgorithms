def binarySearch(num, arr, start, end):  # logn
    """
    Binary search compares the target value to the middle element of the array.
    If they are not equal, the half in which the target cannot lie is eliminated
     and the search continues on the remaining half
    :param num:
    :param arr:
    :param start:
    :param end:
    :return: index

    Complexity O(log n)

    """
    if len(arr) == 0:
        return False
    if start == end:
        if num == arr[start]:
            return start
        else:
            return False
    else:
        mid = (start + end)//2
        if num == arr[mid]:
            return mid
        if num < arr[mid]:
            return binarySearch(num, arr, start, mid)
        else:
            return binarySearch(num, arr, mid+1, end)