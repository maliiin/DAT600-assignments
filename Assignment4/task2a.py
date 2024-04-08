from pulp import LpMinimize, LpProblem, LpVariable, lpSum

# Define the graph parameters
edges = [(1, 2, 10), (1, 3, 5), (2, 3, 15), (2, 4, 10), (3, 4, 5)]
source = 1
sink = 4

# Create the optimization problem
prob = LpProblem("Minimum Cut Problem", LpMinimize)

# Define the decision variables
x = {(u, v): LpVariable(f"x_{u}_{v}", lowBound=0, cat='Binary') for u, v, _ in edges}

# Define the objective function
prob += lpSum([x[e] * c for e, _, c in edges])

# Add constraints
for e, _, _ in edges:
    prob += x[e] <= 1

# Flow conservation constraints
for v in {source, sink}:
    leaving_edges = [(u, v) for u, v, _ in edges if u == v]
    entering_edges = [(u, v) for u, v, _ in edges if v == u]
    prob += lpSum([x[e] for e in leaving_edges]) - lpSum([x[e] for e in entering_edges]) >= 1

# Solve the problem
prob.solve()

# Print the result
print("Minimum cut edges:")
for e, _, _ in edges:
    if x[e].varValue == 1:
        print(e)
