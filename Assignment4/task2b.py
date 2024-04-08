from pulp import *

model = LpProblem("task1", LpMaximize)

# link capasities
sv1 = LpVariable("sv1", lowBound=0, upBound=14, cat="Integer")
sv2 = LpVariable("sv2", lowBound=0, upBound=25, cat="Integer")
v1v4 = LpVariable("v1v4", lowBound=0, upBound=21, cat="Integer")
v1v3 = LpVariable("v1v3", lowBound=0, upBound=3, cat="Integer")
v2v3 = LpVariable("v2v3", lowBound=0, upBound=13, cat="Integer")
v2v5 = LpVariable("v2v5", lowBound=0, upBound=7, cat="Integer")
v3v1 = LpVariable("v3v1", lowBound=0, upBound=6, cat="Integer")
v3v5 = LpVariable("v3v5", lowBound=0, upBound=15, cat="Integer")
v4v3 = LpVariable("v4v3", lowBound=0, upBound=10, cat="Integer")
v4t = LpVariable("v4t", lowBound=0, upBound=20, cat="Integer")
v5v4 = LpVariable("v5v4", lowBound=0, upBound=5, cat="Integer")
v5t = LpVariable("v5t", lowBound=0, upBound=10, cat="Integer")


# objective function
model += sv1 + sv2, "max flow"


# constaints flow in=flow out
model += sv1 + v3v1 == v1v3 + v1v4
model += sv2 == v2v3 + v2v5
model += v1v3 + v2v3 + v4v3 == v3v1 + v3v5
model += v1v4 + v5v4 == v4v3 + v4t
model += v3v5 + v3v5 == v5v4 + v5t
# flow from s==flow in in t
model += sv1 + sv2 == v4t + v5t


model.solve()

print("value of sv1", sv1.varValue)
print("value of sv2", sv2.varValue)
print("value of v1v4", v1v4.varValue)
print("value of v1v3", v1v3.varValue)
print("value of v2v3", v2v3.varValue)
print("value of v2v5", v2v5.varValue)
print("value of v3v1", v3v1.varValue)
print("value of v3v5", v3v5.varValue)
print("value of v4v3", v4v3.varValue)
print("value of v4t", v4t.varValue)
print("value of v5v4", v5v4.varValue)
print("value of v5t", v5t.varValue)

print(sv1.varValue + sv2.varValue)
print(v4t.varValue + v5t.varValue)
