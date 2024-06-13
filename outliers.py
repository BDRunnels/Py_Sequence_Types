# data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
data = []
# del data[0:2] # deletes index 0 up to index 2
# print(data)
# del data[16:] # doesn't work (deleted two items above, which reindexes)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#
# print(data)

# ONLY WORKS IF DATA IS SORTED

    # Process low values in list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print("stop = {}".format(stop)) # for debugging
del data[:stop] # delete values up to stop value, which is why it only works for sorted
print(data)

    # Process high values in list
start = 0
for index in range(len(data) - 1, -1, -1): # starting at end of list, to element - 1, stepping -1 elements backwards
    if data[index] <= max_valid:
        # We have index of last item to keep.
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break
print("start = {}".format(start))
del data[start:]
print(data)
