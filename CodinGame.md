**USERNAME** - uwcshin



**The Descent**
Create a list, mt_list and append every input in the for loop
max(mt_list) represents the biggest number or tallest mountain in the list, doing print(mtlist.index(max(mt_list))) will print the index of the biggest number, a.k.a the mountan number to shoot

```

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop

while True:
    mt_list = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        mt_list.append(mountain_h)
        
    print(mt_list.index(max(mt_list)))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
 
    # The index of the mountain to fire on.
```
    
    **Power of Thor pt1**
    unsuccesful solution
```
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if light_x > initial_tx:
        xmovement = 1 
    elif light_x < initial_tx:
        xmovement = 2
    else:
        xmovement = 3
        
    if light_y > initial_ty:
        ymovement = 1
    elif light_y < initial_ty:
        ymovement = 2
    else:
        ymovement = 3
    
    if xmovement == 1 and ymovement == 3: 
        print("E")
    if xmovement == 1 and ymovement == 1:
        print("SE")
    if xmovement == 1 and ymovement == 2:
        print("NE")
    if xmovement == 2 and ymovement == 3:
        print("W")
    if xmovement == 2 and ymovement == 1:
        print("SW")
    if xmovement == 2 and ymovement == 2:
        print("NW")
    if xmovement == 3 and ymovement == 1:
        print("S")
    if xmovement == 3 and ymovement == 2:
        print("N")
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # A single line providing the move to be made: N NE E SE S SW W or NW
 
```
