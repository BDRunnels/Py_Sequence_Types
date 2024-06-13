# t = ("a", "b", "c") # valid t = "a", "b", "c" without parentheses
# print(t)
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# meta1 = list(metallica)
# print(meta1)
#
# meta1[0] = "Master of Puppets"
# print(meta1)
#
# metallica = tuple(meta1)
# print(metallica)
title, artist, year = metallica
print(title, artist, year, sep=", ", end=".\n")

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)

# PUTTING ALL ALBUMS INTO A LIST OF TUPLES
all_albums = [welcome,
              bad,
              budgie,
              imelda,
              metallica,
              ]

print(len(all_albums))

for name, artist, year in all_albums:
    print("Album: {}\n\tArtist: {}\n\tYear: {}"
          .format(name, artist, year))

# OR
for album in all_albums:
    name, artist, year = album
    print(len(album))
    print("Album: {}\n\tArtist: {}\n\tYear: {}"
          .format(name, artist, year))
