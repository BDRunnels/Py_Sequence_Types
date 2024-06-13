pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers) # sorted() returns a new list
print(sorted_numbers)
print(numbers)

numbers.sort() # .sort() modifies original list in place, returns None.
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog"
                        .casefold())
print(missing_letter)

# SORTING LIST OF NAMES
names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)
