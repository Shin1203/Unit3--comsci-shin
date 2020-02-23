**LIST PRACTISE SNAKIFY**

Even indices
-Because input is given in one line - (1 2 3 4 5), use .split() when defining a, it will split the numbers based on spacing.
```
a = input().split()
for i in range(len(a)):
    if i%2 == 0:
        print(a[i])
```

Even element
-To make sure every element in list a is an integer, a is defined as follows
-input is still in one line, so split() is needed.
```
a = [int(s) for s in input().split()]
for i in a:
    if i%2 == 0:
        print(i)
```

Greater than Previous
```
a = [int(s) for s in input().split()]
for i in range(len(a)):
    if i > 0:
        if a[i] > a[i-1]:
         print(a[i])
```

Neighbors of the same sign
```
a = [int(s) for s in input().split()]
for s in range(1, (len(a))):
    if a[s]*a[s-1] > 0:
        print(a[s-1])
        print(a[s])
        break
```

Greater than Neighbours
```
a = input().split()
counter = 0
for i in range(1, (len(a)-1)):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        counter+=1

print(counter)
```

