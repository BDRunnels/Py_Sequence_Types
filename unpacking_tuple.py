a = b = c = d = e = f = 42
print(c)

# Unpacking a tuple.
x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1, 2, 76 # data represents tuple
x, y, z = data
print(x)
print(y)
print(z)

# Can unpack any sequence type...
    # LIST
print("Unpacking a list")

data_list = [12, 13, 14]
data_list.append(15) # breaks code, must include amount of variables for amount of items in list

p, q, r = data_list
print(p, q, r)
