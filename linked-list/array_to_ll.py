class Node:
    def __init__(self, data=0, next: 'Node' = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add(self, num: int):
        el = Node(num)
        if self.head is None:
            self.head = el
            self.tail = el
            return
        self.tail.next = el
        self.tail = el

# Utility function to convert list to LinkedList
def list_to_linkedlist(arr: list[int]) -> Node:
    ll = LinkedList()
    for el in arr:
        ll.add(el)
    return ll.head

# Utility function to traverse and print LinkedList
def print_linkedlist(head: Node):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()  # to move to a new line after traversal

# Testing the code
my_list = [4, 2, 5, 1]
linked_list_head = list_to_linkedlist(my_list)
print_linkedlist(linked_list_head)