''' Module contains questions and solutions to classic
    string related Coding Interview Questions 
'''

# Table of contents
# Q1: How can you reverse a string
# Q2: Determine if a string is a palindrome
# Q3: Determine instances of character in a given string


# Question : How can you reverse a string
def reverse_string(s):
    """ Returns reverse of string """
    # Asymptotic Time Complexity: O(n)
    # Auxillary Space Complexity: O(1)
    
    return s[::-1]


# Question 2: Determine if a string is a palindrome
def palindrome(s):
    """ Returns True if string is palidrome; False otherwise """
    # Asymptotic Time Complexity: O(n)
    # Auxillary Space Complexity: O(1)
    
    for i in range(len(s)// 2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True


# Question 3: Determine instances of character in a given string 
def character_instances_1(s, c):
    """ Returns counr of character instances in string 
        Note: This pattern can be used for general character count
        and is not Optimal
    """
    # Asymptotic Time Complexity: O(n)
    # Auxillary Space Complexity: O(n) - due to dictionary

    character_counter = {}

    for i in s:
        if i in character_counter:
            character_counter[i] += 1
        else:
            character_counter[i] = 1
    return character_counter.get(c, 0)

def character_instances_2(s, c):
    """ Returns counr of character instances in string 
        Note: Optimal
    """
    # Asymptotic Time Complexity: O(n)
    # Auxillary Space Complexity: O(1)

    counter = 0
    
    for char in s:
        if char == c:
            counter += 1
    
    return counter

    
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



if __name__ == "__main__":
    print(move_zeroes_3([1,10,20,0,59,63,0,88,0]))