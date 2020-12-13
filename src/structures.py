''' Module contains questions and solutions to classic
    data structure related Coding Interview Questions 
'''

###### Table of contents ######
### Linked List ###
# Q1: Reverse Linked List
# Q2: Find middle element of a Linked List (in single pass)


### Linked Lists ###
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        result = ""
        current = self.head
        while current:
            result+= str(current.data) + ' '
            current = current.next
        return result


    # Question 1a: Can you reverse a LinkedList (defined below)
    def reverse(self):
        ''' Reverses Linked List iteratively '''

        current_node = self.head
        previous_node = None

        # Edge case
        if current_node is None:
            return
            
        next_node = current_node.next

        while next_node is not None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next
        
        # Last step
        current_node.next = previous_node
        self.head = current_node

    # Question 1b: Can you reverse a LinkedList (defined below)
    def reverse_recursive(self):
        ''' Reverses Linked List recursively '''
        previous = None
        current = self.head
        def reverse(self, previous_node, current_node):
            if current_node.next is None:
                current_node.next = previous_node
                self.head = current_node
                return 
            else:
                t = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = t
                reverse(self, previous_node, current_node)

        reverse(self, previous, current)


    # Q2: Find middle element of a Linked List (in single pass)
    def middle_element(self):
        ''' Finds middle element of Linked List '''
        
        one_step = self.head
        two_step = self.head
    
        # Edge case
        if one_step is None:
            return
            
        counter = 0

        while two_step is not None:
            two_step = two_step.next
            
            counter += 1

            if counter % 2 == 0:
                one_step = one_step.next
        
        return one_step.data


    # Q3: Find the start of a cycle in Linked List (if it exists)
    def start_cycle(self):
        ''' Finds start element of Linked List cycle; 
            returns None if no cycle exists
        '''
        # TODO

































