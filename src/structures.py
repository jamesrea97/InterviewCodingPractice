''' Module contains questions and solutions to classic
    data structure related Coding Interview Questions 
'''

# Table of contents
# Q1: Reverse Linked List



# Question 1: Can you reverse a LinkedList (defined below)
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

    ''' Solution in reverse() method '''

    def reverse(self):
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

        


def linked_list_driver():
    ll_edge_case = LinkedList()
    
    ll = LinkedList()
    ll.append(7)
    ll.append(1)
    ll.append(30)
    ll.append(4)

    
    print('Forward Linked List 1: ' + ll.display())
    ll.reverse()
    print('Backward Linked List 1: ' + ll.display())

    print('\nForward Linked List 2:' + ll_edge_case.display())
    ll_edge_case.reverse()
    print('Backward Linked List 2: ' + ll_edge_case.display())
