import matplotlib.pyplot as pyplot
z = []
tick = 0.04

for i in range(1000):
    z.append(-2 + tick*i)

n = [(z + 1)**2 - 1 for z in i]

pyplot.plot(z, n)

pyplot.show()
