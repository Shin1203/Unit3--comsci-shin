# thisprogram will tell you the dog's age in dog years.
print("input dog's age in human years")
humanyears = int(input())
dogyears = 0.0
for i in range(1, humanyears+1):
    if i < 3:
        dogyears += 10.5
    if i > 2:
        dogyears += 4

print("The dogs age in dogyears is", dogyears)
