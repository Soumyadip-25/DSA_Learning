# Remove duplicates from a sorted Linked List
# Remove repeated elements from a sorted linked list.

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

current = head

while current is not None and current.next is not None:

    if current.data == current.next.data:
        current.next = current.next.next
    else:
        current = current.next

print("Linked List after removing duplicates:")

current = head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")