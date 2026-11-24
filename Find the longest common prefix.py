# Find the longest common prefix
# Find the longest starting portion shared by all given strings.

n = int(input("Enter number of strings: "))

words = []

for i in range(n):
    word = input("Enter string: ")
    words.append(word)

if n == 0:
    print("No strings provided")

else:
    prefix = words[0]

    for word in words[1:]:

        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                break

    print("Longest common prefix:", prefix)