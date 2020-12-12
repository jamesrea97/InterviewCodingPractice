''' Module contains questions and solutions to classic
    array-of-int related Coding Interview Questions 
'''

# Table of contents
# Q1: 'Move Zeros to Left'

# Question 1: 'Move Zeros to Left' - curtorsy of Facebook
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


