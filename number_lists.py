empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# CONCATENATE / CREATING LISTS
numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers) # original NOT MODIFIED
#
# digits = list("432985617")
# print(digits)
#
# # more_numbers = list(numbers)
# # more_numbers = numbers[:] # SLICE TO COPY LIST
# more_numbers = numbers.copy() # MOST COMMON WAY
# print(more_numbers)
# print(numbers is more_numbers) # if 2 lists point to same object
# print(numbers == more_numbers) # if list contains same items in same order



# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("s"))

# SORTING LIST
# even.extend(odd) # appends iterable to list
# print(even)
# another_even = even
# print(another_even)
#
# even.sort(reverse=True) # doesn't create new copy, sorts IN PLACE (modifies original)
# print(even)
# print(another_even)
