# this code graphs coronavirus cases and gold prices of march, and finds correlation coefficient
import matplotlib.pyplot as pyplot

coronaviruscases = [88585, 90443, 93016, 95314, 98425, 102050, 109991, 114381, 118948, 126214, 134509, 145416, 169511,
                    182431, 198161, 218843, 244988, 275680, 305132, 337612, 379105, 422940, 471497, 532491, 597044,
                    663805, 724220, 786006, 859798]
goldprices = [1564, 1592, 1592, 1641, 1666, 1671, 1671, 1671, 1675, 1659, 1641, 1589, 1516, 1516, 1516, 1486, 1525,
              1477, 1479, 1484, 1484, 1484, 1567, 1660, 1632, 1650, 1624, 1624, 1624, 1622, 1583]
pyplot.scatter(coronaviruscases, goldprices)
pyplot.show()
