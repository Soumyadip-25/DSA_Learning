# Find the middle element of a Linked List
# Find the middle node of a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n = int(input("Enter number of nodes: "))

head = None
tail = None

for i in range(n):
    num = int(input("Enter value: "))
    new_node = Node(num)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

if slow is not None:
    print("Middle element:", slow.data)
else:
    print("Linked List is empty")