# Implement a Queue using a Python List
# A queue follows FIFO (First In, First Out).

queue = []

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter value: "))
        queue.append(num)
        print("Element inserted")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Removed element:", queue.pop(0))

    elif choice == 3:
        print("Queue:", queue)

    elif choice == 4:
        break

    else:
        print("Invalid choice")