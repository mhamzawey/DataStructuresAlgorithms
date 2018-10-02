def mergeSort(A):
    """
    The mergeSort function begins by asking the base case question.
    If the length of the list is less than or equal to one, then we
     already have a sorted list and no more processing is necessary.
     If, on the other hand, the length is greater than one, then we
      use the Python slice operation to extract the left and right halves.
       It is important to note that the list may not have an even number of items.
       That does not matter, as the lengths will differ by at most one
    Once the mergeSort function is invoked on the left half and the right half
     it is assumed they are sorted. The rest of the function is responsible for
      merging the two smaller sorted lists into a larger sorted list. Notice that
       the merge operation places the items back into the original list (A) one at a
        time by repeatedly taking the smallest item from the sorted lists.
    :param A: []
    :return: A: []

    Complexity: nlog(n)
    """
    print("Splitting ",A)
    if len(A) >1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i <len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j <len(right):
            A[k] = right[j]
            j += 1
            k += 1
        print("Merging ",A)

    return A







arr = [1,2,6,7,8,10,4,13,18,29,79,54,32,21]
print(mergeSort(arr))

