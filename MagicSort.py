import math

def insertionsort(L, left=0, right=None):
    #Loop through L comparing right value with previous, if right is smaller, then switch
    if right is None:
        right = len(L) - 1

    for i in range(left + 1, right + 1):
        key_item = L[i]
        j = i - 1
        while j >= left and L[j] > key_item:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key_item

def reverse_list(L, left, right):
        #Reverse list L from left to right
        while left < right:
            L[left], L[right] = L[right], L[left]
            left += 1

def linear_scan(L):
     #Linear scan of list L to return value that indicates any edge cases that apply
    n = len(L)
    
    #Checks list for already sorted
    sorted_flag = True
    for i in range(1, n):
        if L[i] < L[i-1]:
            sorted_flag = False
            break
    if sorted_flag:
        return 'already_sorted'
    
    #Checks list for reverse sorted
    reverse_flag = True
    for i in range(1, n):
        if L[i] > L[i-1]:
            reverse_flag = False
            break
    if reverse_flag:
        return 'reverse_sorted'
    
    #Checks list for 5 items at most out of place
    out_of_place_count = 0
    for i in range(1, n):
        if L[i] < L[i-1]:
            out_of_place_count += 1
        if out_of_place_count > 5:
            break
    if out_of_place_count <= 5:
        return 'insertion_sort'
    
    return 'none'

def quicksort(L, left, right, rec_max=None):
    if left >= right:
        return

    # Use insertion sort for small partitions (≤10 elements)
    if right - left + 1 <= 10:
        insertionsort(L, left, right)
        return

    if rec_max is None:
        rec_max = int(math.log2(right - left + 1) + 1)

    if rec_max == 0:
        mergesort(L, left, right)
        return

    pivot_idx = right
    pivot_val = L[pivot_idx]

    # Partition
    i = left - 1
    for j in range(left, right):
        if L[j] <= pivot_val:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[pivot_idx] = L[pivot_idx], L[i + 1]

    quicksort(L, left, i, rec_max - 1)
    quicksort(L, i + 2, right, rec_max - 1)


def mergesort(L, left=0, right=None):
    if right is None:
        right = len(L) - 1
    if left >= right:
        return
    
    mid = (left + right) // 2
    mergesort(L, left, mid)
    mergesort(L, mid + 1, right)

    # Merge step (in-place modification)
    merged = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if L[i] <= L[j]:
            merged.append(L[i])
            i += 1
        else:
            merged.append(L[j])
            j += 1

    # Add remaining elements
    while i <= mid:
        merged.append(L[i])
        i += 1
    while j <= right:
        merged.append(L[j])
        j += 1

    # Copy merged list back to L
    L[left:right + 1] = merged

def magic_sort(L):
    algorithms_used = set()
    scan_result = linear_scan(L)

    if scan_result == 'already_sorted':
        return algorithms_used

    if scan_result == 'reverse_sorted':
        reverse_list(L, 0, len(L) - 1)
        algorithms_used.add('reverse_list')
        return algorithms_used

    if scan_result == 'insertion_sort':
        insertionsort(L, 0, len(L) - 1)
        algorithms_used.add('insertion_sort')
        return algorithms_used

    # Otherwise, use quicksort with adaptive depth
    max_depth = math.ceil(math.log2(len(L))) + 1
    quicksort(L, 0, len(L) - 1, max_depth)
    algorithms_used.add('quicksort')

    return algorithms_used

