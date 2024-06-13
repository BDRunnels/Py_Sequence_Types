# Python executes all data in the file you import
# (commented out all non-definition data / print statements)
from nested_data import albums

# All caps denotes constant in Python.
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please select an Album (Invalid choice to exit):")
        # must enclose unpacked items in parentheses with enumerate
        # it returns 2 values (index, item)
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {} by {}".format(index + 1, title, artist))

        # SAME AS ABOVE
    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index, title, artist,  year, songs)
    
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        print("Invalid Choice. Exiting Program.\n")
        break

    print("Please select a Song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))

    print("=" * 40)
