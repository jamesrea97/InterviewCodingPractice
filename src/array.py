''' Module contains questions and solutions to classic
    array-of-int related Coding Interview Questions 
'''

# Table of contents
# Q1: 'Move Zeros to Left'
# Q2: How to find the missing number in a given array of 1 to n





# Q1: 'Move Zeros to Left' - curtorsy of Facebook
'''
Given an integer array, move all 0s to the 
left while maintaning order of other elements
'''
def move_zeroes_1(arr):
    """" Returns array with all zeroes moved to the left,
        preserving ordering
        Note: This method is similar to Bubble sort and
        trades low space complexity for higher time complexity
    """
    # Asymptotic Time Complexity: O(n^2)
    # Auxillary Space Complexity: O(1)

    for i in range(len(arr)):
        if arr[i] == 0:
            j = i - 1
            while j > -1:
                if arr[j] != 0:
                    t = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = t
                    j -= 1
                else:
                    break
    return arr

def move_zeroes_2(arr):
    """" Returns array with all zeroes moved to the left,
        preserving ordering
        Note: This method trades higher space complexity for lower
        time complexity
    """
    # Asymptotic Time Complexity: O(n)
    # Auxillary Space Complexity: O(n)

    zeroes = []
    others = []

    for i in range(len(arr)):
        if arr[i] == 0:
            zeroes.append(arr[i])
        else:
            others.append(arr[i])
    
    return zeroes + others

def move_zeroes_3(arr):
    """" Returns array with all zeroes moved to the left,
        preserving ordering. Optimal
    """
    # Asymptotic Time Complexity: O(n)
    # Auxillary Space Complexity: O(1)

    read = len(arr)-1
    write = len(arr)-1

    while read > -1:
        if arr[read] != 0:
            arr[write] = arr[read]
            write -= 1
        read -= 1  
    while write > -1:
        arr[write] = 0
        write -= 1

    return arr


# Question 2: How to find the missing number in a given array of 1 to n
'''
Given an integer array with numbers 1 to n, find the missing number (changed to a zero)
'''
def missing_number(arr):
    """" Returns missing element 
        Note: Optimal
    """
    # Asymptotic Time Complexity: O(n)
    # Auxillary Space Complexity: O(1)

    sum_array = 0
    sum_total = 0
    for i in range(len(arr)):
        sum_array+= arr[i]
        sum_total += (i + 1)

    return sum_total - sum_array
    
# Question 3: How to find the minimum and maximum in an array
def find_min_max(arr):
    """" Returns min and max of array
        Note: Optimal
    """
    # Asymptotic Time Complexity: O(n)
    # Auxillary Space Complexity: O(1)

    min_index = 0
    max_index = 0

    for i in range(len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
        if arr[i] < arr[min_index]:
            min_index = i
    
    return arr[min_index], arr[max_index]


# Question 4: How to find the pair of integers that sum up to a a value
def find_pair_sum(arr, s):
    """" Returns a pair of integers that sum to s; None otherwise
        Note: higher space complexity traded for lower time complexity
    """
    # Asymptotic Time Complexity: O(n)
    # Auxillary Space Complexity: O(n)

    sum_map = {}

    for i in range(len(arr)):
        if s-arr[i] in sum_map:
            return s-arr[i], arr[i]
        else:
            sum_map[s-arr[i]] = 0
            sum_map[arr[i]] = 0
    
    return None
