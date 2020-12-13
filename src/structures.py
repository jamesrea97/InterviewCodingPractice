''' Module contains questions and solutions to classic
    data structure related Coding Interview Questions 
'''

###### Table of contents ######
### Linked List (LL) ###
# Q1: Reverse Linked List
# Q2: Find middle element of a Linked List (in single pass)
### Binarty Search Tree (BST) ###
# Q1: Implement BST element addition
# Q2: Reverse BST 
# Q3: Count number of leaves

### Linked Lists (LL) ###
## Note On structure
# Traditional LL has is a singally linked chain of Nodes. 
# Each Node contains data and pointer to next Node. 
# LL starts with head and ends with Node
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = LinkedListNode(data)
            self.last_node = self.head
        else:
            self.last_node.next = LinkedListNode(data)
            self.last_node = self.last_node.next
 
    def display(self):
        result = ""
        current = self.head
        while current:
            result+= str(current.data) + ' '
            current = current.next
        return result


    # Question 1a: Can you reverse a LL (defined below)
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

    # Question 1b: Can you reverse a LL (defined below)
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


    # Q2: Find middle element of a LL(in single pass)
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





### Binary Search Tree ###
## Note On structure
# Traditional BST is a rooted tree of Nodes 
# Each Node contains
#       A key 
#       A left child sub-tree of Node containing only lower keys.
#       A right child sub-tree of Node containing only higher keys. 
class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # Q1: Add
    def add_element(self, value):
        ''' Adds element to BST ''' 
        current_node = self
        
        while current_node is not None:
            if value < current_node.key:
                if current_node.left is None:
                    current_node.left = BinarySearchTree(value)
                    break
                else:
                    current_node = current_node.left
                
            else:
                if current_node.right is None:
                    current_node.right = BinarySearchTree(value)
                    break
                else:
                    current_node = current_node.right

    def display(self):
        ''' Displays BST (curtosy of https://stackoverflow.com/questions/
                34012886/print-binary-tree-level-by-level-in-python)''' 
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2



    # Q2: Reverse BST
    def reverse(self):
        ''' Reverses BST i.e. left child and right child inverse '''
    
        def recursive_reverse(node):
            if node.left is None and node.right is None:
                return
            else:
                t = node.left
                node.left = node.right
                node.right = t
                recursive_reverse(node.left)
                recursive_reverse(node.right)

        recursive_reverse(self)

            


























