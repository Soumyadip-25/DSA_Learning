# Reverse a Linked List
# Reverse the direction of a singly linked list.

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

prev = None
current = head

while current is not None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

head = prev

print("Reversed Linked List:")

current = head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")