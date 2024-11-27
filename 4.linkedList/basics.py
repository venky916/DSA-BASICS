class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.dummy_head = ListNode()  # Dummy head node
        self.tail = self.dummy_head    # Tail initially points to dummy head

    # Insert at the end of the linked list
    def insert_end(self, value):
        new_node = ListNode(value)
        self.tail.next = new_node
        self.tail = new_node  # Move the tail to the new node
    
    def insert_at_beginning(value):
        new_node = ListNode(value)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node


    # Display the linked list
    def display(self):
        current = self.dummy_head.next  # Skip dummy head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    # Find the length of the linked list
    def length(self):
        length = 0
        current = self.dummy_head.next  # Skip dummy head
        while current:
            length += 1
            current = current.next
        return length

# using stack
# for all reversing always use stack
def reverse_list_st(head):
    stack =[]
    curr = head

    while curr:
        stack.append(curr.key)
        curr= curr.next
    
    curr = head

    while curr:
        curr.key = stack.pop()
        curr = curr.next
    
    return head

def reverse_linked_list(head):
    prev = None
    current =head

    while current:
        # these four get node, nxt,prev
        nxt = current.next
        prev = current

        current.next = prev
        current = next_node

    head = prev
    return head
# recursive
def reverse_recursive(curr,prev=None):
    if curr == None:
        return prev
    nxt = curr.next
    curr.next = prev
    return reverse_recursive(nxt,curr)
# recursive
def reversList(head):
    if head == None:
        return None
    
    if head.next == None:
        return head
    
    rest_head = reversList(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None

    return rest_head
