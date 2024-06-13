panagram = """The quick brown
fox jumps\tover
the lazy dog"""

words = panagram.split() # returns a list from a string (ie array from string)
print(words)

numbers = "9,223,372,036,854,775,807"
values = numbers.split(",")
print(values)

#1 converting values from string to int - mutating entire list
for index in range(len(values)):
    values[index] = int(values[index])

print(values)

#2 create new list and append integers to it
integer_values = []
for value in values:
    integer_values.append(int(value))

print(integer_values)

user_input = input("Please enter 3 numbers separated by a comma: ")
user_numbers = user_input.split(",")

int_values = []
for number in user_numbers:
    int_values.append(int(number))

a,b,c = int_values # unpacking, can use variables in order to grab values from list (very cool)

print("Answer of {} + {} - {} = {}".format(a,b,c,a+b-c))
