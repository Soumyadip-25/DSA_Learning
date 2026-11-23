# Implement a Queue using Two Stacks
# A queue follows FIFO (First In, First Out), while a stack follows LIFO (Last In, First Out).

stack1 = []
stack2 = []

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        num = int(input("Enter value: "))
        stack1.append(num)

        print("Element inserted")

    elif choice == 2:

        if len(stack2) == 0:

            while len(stack1) > 0:
                stack2.append(stack1.pop())

        if len(stack2) == 0:
            print("Queue is empty")
        else:
            print("Removed:", stack2.pop())

    elif choice == 3:

        queue = stack2[::-1] + stack1
        print("Queue:", queue)

    elif choice == 4:
        break

    else:
        print("Invalid choice")