''' Module contains questions and solutions to classic
    string related Coding Interview Questions 
'''

# Table of contents
# Q1: How can you reverse a string
# Q2: Determine if a string is a palindrome
# Q3: Determine instances of character in a given string


# Question 1: How can you reverse a string
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
