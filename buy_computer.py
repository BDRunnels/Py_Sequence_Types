available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "HDMI Cable",
                   "DVD Drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(i)
current_choice = 999
computer_parts = [] # create empty list

while current_choice != 0:
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in list, remove it
            print("Removing {}".format(available_parts[index]))
            computer_parts.remove(chosen_part)
        else:
            # it's not in list, add it
            print("Adding {}".format(available_parts[index]))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}\n".format(computer_parts))
    elif current_choice != 999 and current_choice not in valid_choices:
        print("INVALID INPUT. Please choose again.")
    else:
        print("Please add options from list below: ")
        # for part in available_parts:
        #     print("{0}: {1}".format(
        #         available_parts.index(part) + 1,
        #         part
        #     ))
        # MORE EFFICIENT
        # Python won't have to look up index using enumerate
        # enumerate returns index and item (arguments 1 and 2)
        for index, part in enumerate(available_parts):
            print("{0}: {1}".format(index + 1, part))

    current_choice = int(input())

print(computer_parts)
