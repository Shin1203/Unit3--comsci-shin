**USERNAME** - uwcshin



**The Descent**
Create a list, mt_list and append every input in the for loop
max(mt_list) represents the biggest number or tallest mountain in the list, doing print(mtlist.index(max(mt_list))) will print the index of the biggest number, a.k.a the mountan number to shoot
``
import sys
import math

The while loop represents the game.
Each iteration represents a turn of the game
 where you are given inputs (the heights of the mountains)
 and where you have to print an output (the index of the mountain to fire on)
 The inputs you are given are automatically updated according to your last actions.


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
``
    
    
