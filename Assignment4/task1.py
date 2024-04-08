# kilde http://benalexkeen.com/linear-programming-with-python-and-pulp-part-3/
# dato 13.03.24

from pulp import *

model = LpProblem("task1", LpMaximize)

x = LpVariable("X", lowBound=10, cat="Integer")
y = LpVariable("Y", lowBound=0, cat="Integer")

# objective function
model += 505 / 3 * x + 770 / 3 * y, "profit"

# constaints
model += x * 1 / 4 + y * 1 / 3 <= 40
model += x * 1 / 3 + y * 1 / 2 <= 35

model.solve()

print("value of x", x.varValue)
print("value of y", y.varValue)
print(pulp.value(model.objective))
