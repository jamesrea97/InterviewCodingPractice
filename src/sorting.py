''' 
Module contains classic sorting algorithms
'''

###### Table of contents ######
# 1. Insertion Sort
# 2. Selection Sort
# 3. Merge Sort 
# 4. QuickSort TODO
# 5. Heap Sort TODO
# 6. Bubble Sort


# 1. Insertion Sort
def insertion_sort(arr):
    ''' Returns sorted arr '''
    # Asymptotic Time Complexity: Best O(N) [Sorted] Worst O(n^2) [Unsorted] 
    # Auxillary Space Complexity: O(1)

    # Idea: Build array up, inserting the elements in the right places

    i = 0

    while i < len(arr):
        j = i
        while arr[j] > arr[j- 1]:
                t = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = t
                if j - 1 >= 0:
                    j-= 1
        i += 1
    
    return arr


# 2. Selection Sort
def selection_sort(arr):
    ''' Returns sorted arr '''
    # Asymptotic Time Complexity: Always O(n^2)
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


# 3 Merge Sort
def merge_sort(arr):
    ''' Returns sorted arr '''
    # Asymptotic Time Complexity: Always - O(nlog(n))
    # Auxillary Space Complexity: O(n)

    # Idea: separate into size 1 length arrays and merge 2 togehter, building
    # up sorted array


    def recursive_merge_sort(arr):
        ''' Internal driver method for merge sort. 
            Note: Separate firt and then merge
        '''
        if len(arr) < 2:
            return arr
        else:
            mid = len(arr) // 2

            left = recursive_merge_sort(arr[:mid])
            right = recursive_merge_sort(arr[mid:])

            return merge(left, right)
    
    def merge(left, right):
        ''' Internal method that merges two sub-arrays in increasing order '''
        a = []
        i = 0
        j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a.append(left[i])
                i += 1
            else:
                a.append(right[j])
                j += 1
        while i < len(left):
            a.append(left[i])
            i += 1
        while j < len(right):
            a.append(right[j])
            j += 1

        return a
    
    return recursive_merge_sort(arr)



