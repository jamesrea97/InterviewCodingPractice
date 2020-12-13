''' Module contains classic sorting algorithms
'''

# Table of contents
# 1. Insertion Sort
# 2. Selection Sort
# 3. Merge Sort
# 4. QuickSort
# 5. TODO Heap Sort
# 6. Bubble Sort


# 1. Insertion Sort
def insertion_sort(arr):
    ''' Returns sorted arr '''
    # Asymptotic Time Complexity: O(n^2)
    # Auxillary Space Complexity: O(1)

    # Idea: Build array up, inserting the elements in the right places

    i = 0

    while i < len(arr):
        j = i
        if j - 1 >= 0:
            while arr[j] < arr[j- 1]:
                t = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = t
                j-= 1
        i += 1
    
    return arr


# 2. Selection Sort
def selection_sort(arr):
    ''' Returns sorted arr '''
    # Asymptotic Time Complexity: O(n^2)
    # Auxillary Space Complexity: O(1)

    # Idea: Select location of element and swap

    for i in range(len(arr)):
        index_lowest = i
        for j in range(i, len(arr)):
            if arr[j] < arr[index_lowest]:
                index_lowest = j
        t = arr[i]
        arr[i] = arr[index_lowest]
        arr[index_lowest] = t
    
    return arr

