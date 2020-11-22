"""
Instructions
You are going to write a program which will mark a spot with an X.

The map is made of 3 rows of blank squares.

  1      2      3
1 ['⬜️', '⬜️', '⬜️']
2 ['⬜️', '⬜️', '⬜️']
3 ['⬜️', '⬜️', '⬜️']

Your program should allow you to enter the position of the treasure using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

Example Input 1
column 2, row 3 would be entered as:
=> 23

print 
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
['⬜️', '⬜️', '⬜️']
"""

# Creating the box for map with emoji
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Horizontal & Vertical initilize Postion 0
horizonal = int(position[0])
vertical = int(position[0])

# selecting row and replace selected row with "x"
selected_row = map[vertical - 1]
selected_row[horizonal - 1] = "X"

# Printing the tresure map
print(f"{row1}\n{row2}\n{row3}")
