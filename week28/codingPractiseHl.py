import matplotlib.pyplot as pyplot
import csv
import numpy as np
# code below opens total cases csv file, as dt
with open("total_cases.csv") as dt:
    dates = []
    totalcases = []
    japantotalcases = []
    testcounter = 0
    # code below w
    values = csv.reader(dt, delimiter=",", )
    for lines in values:
        dates.append(lines[0])
        totalcases.append(lines[1])
        japantotalcases.append(lines[79])
#code below deletes the "world" and "date" respectively from the list, to only show important values
del totalcases[0]
del dates[0]
del japantotalcases[0]
# instead of making X of the graph filled with "2020/m/d" values, create relativedate variable, use it in for loop to add relative number of days since corona outbreak to number of days list.
relativedate = 1
numberofdays = []

for chars in dates:
    numberofdays.append(relativedate)
    relativedate+=1
print(numberofdays)


pyplot.plot(numberofdays, japantotalcases, totalcases)
pyplot.ylabel("Corona cases Japan(BLUE) vs World(Orange)")
pyplot.xlabel("Days since outbreak")
# the below xticks and yticks sets difference between every x and y value shown on axis, first and second number represent first value and final
pyplot.xticks(np.arange(0,58, 1.0))
# same process with y axis
pyplot.show()
