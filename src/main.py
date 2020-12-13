''' Driver module for Coding Interview Questions '''

import array
import string
import structures
import sorting



def linked_list_reverse_driver(recursive = False):
    ll_edge_case = structures.LinkedList()
    
    ll = structures.LinkedList()
    ll.append(7)
    ll.append(1)
    ll.append(30)
    ll.append(4)

    
    print('Forward Linked List 1: ' + ll.display())
    ll.reverse_recursive() if recursive else ll.reverse()
    print('Backward Linked List 1: ' + ll.display())

    print('\nForward Linked List 2:' + ll_edge_case.display())
    ll_edge_case.reverse()if recursive else ll_edge_case.reverse()
    print('Backward Linked List 2: ' + ll_edge_case.display())


def linked_list_middle_element_driver():
    ll_edge_case = structures.LinkedList()
    
    ll = structures.LinkedList()
    ll.append(7)
    ll.append(1)
    ll.append(30)
    ll.append(4)

    print('Linked List:' + ll.display())
    print('Middle element of Linked List: ' + str(ll.middle_element()))

    print('Linked List:' + ll_edge_case.display())
    print('Middle element of Linked List: ' + str(ll_edge_case.middle_element()))


if __name__ == "__main__":
    linked_list_reverse_driver(True)


