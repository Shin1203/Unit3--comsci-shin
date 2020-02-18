#generate random numbers and graph them along y axis
import math
from random import seed
from random import randint
import matplotlib.pyplot as pyplot
seed(1)
x = [i for i in range(0, 1000)]
y = []
total = 0
counter = 0
for num in x:
    num =(randint(0, 100))
    y.append(num)
    total += num
pyplot.plot(x. y)

average = total/1000

#graph a sine graph
start = -10
y = 0
z = []
for num in range (-100, 100)
    start += 0.1
    z.append(start)
pyplot.plot(14 * math.sin(0.5 * z), y)

pyplot.show



