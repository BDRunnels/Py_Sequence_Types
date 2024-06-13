# Unpacking the tuple (t) that enumerate creates
for index, char in enumerate("abcdefgh"):
    print(index, char)

print()

# Prints a tuple of (index, item),
for t in enumerate("abcdefgh"):
    # index, char = t
    # print(index, char)
    print(t)

index, character, = (0, 'a')
print(index)
print(character)
