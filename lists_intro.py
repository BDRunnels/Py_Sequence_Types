computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

# for part in computer_parts:
#     print(part)
#
# print()
# print(computer_parts[2])
#
# print(computer_parts[0:3]) #  returns items 0,1,2 in list
# print(computer_parts[-1]) #  returns last item in list
print(computer_parts)
# computer_parts[3] = "trackball"

print(computer_parts[3:]) # prints index 3 to end of list
computer_parts[3:] = ["trackball"]
print(computer_parts)
