# Check balanced parentheses

s = input("Enter brackets: ")

stack = []
balanced = True

for char in s:

    if char in "({[":
        stack.append(char)

    elif char in ")}]":

        if len(stack) == 0:
            balanced = False
            break

        top = stack.pop()

        if (char == ')' and top != '(') or \
           (char == '}' and top != '{') or \
           (char == ']' and top != '['):

            balanced = False
            break

if len(stack) != 0:
    balanced = False

if balanced:
    print("Balanced")
else:
    print("Not Balanced")