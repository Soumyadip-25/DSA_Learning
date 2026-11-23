# Detect a cycle in a Linked List
# Check whether a linked list contains a cycle (loop).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating a linked list
n = int(input("Enter number of nodes: "))

head = None
tail = None
nodes = []

for i in range(n):
    num = int(input("Enter value: "))
    new_node = Node(num)
    nodes.append(new_node)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

# Create a cycle if requested
choice = input("Create a cycle? (yes/no): ").lower()

if choice == "yes" and n > 1:
    pos = int(input("Enter position to connect last node (0-based): "))

    if 0 <= pos < n:
        tail.next = nodes[pos]

# Detect cycle
slow = head
fast = head

cycle = False

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        cycle = True
        break

if cycle:
    print("Cycle detected")
else:
    print("No cycle detected")