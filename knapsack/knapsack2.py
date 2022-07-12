"""
Tutorial source: https://github.com/brentertainer/pyomo-tutorials/blob/master/introduction/01-binary-knapsack.ipynb

Mathematical model:
Objective function: max 3x_1 + 4x_2 + 5x_3 + 8x_4 + 9x_5
Constraints:
Constraint 1: 2x_1 + 3x_2 + 4x_3 + 5x_4 + 9x_5 <= 20
Constraint 2: x_1, x_2, x_3, x_4, x_5 E {0, 1}
"""

# Import framework
import pyomo.environ as pe 
import pyomo.opt as po 

# Setting the solver
solver = po.SolverFactory('glpk') # GNU Linear Programing kit

# Solving a Knapsack problem
model = pe.ConcreteModel()

# Set of items
model.N = pe.RangeSet(1, 5) 

# print(set(model.N))

c = {1: 3, 2: 4, 3 : 5, 4 : 8, 5 : 9} # Cost 
a = {1 : 2, 2 : 3, 3 : 4, 4 : 5, 5 : 9} # size
b = 20

# Declaring and intialising the parameters
model.c = pe.Param(model.N, initialize=c)
model.a = pe.Param(model.N, initialize=a)
model.b = pe.Param(initialize=b)

# print(model.component)
# print(model.c)
# print(model.b) # b
#print(model.b.value)
#print(pe.value(model.b)) # 20

# Define the variable
model.x = pe.Var(model.N, domain=pe.Binary)

# State the objective function
obj_expr = sum(model.c[i] * model.x[i] for i in model.N)
model.obj = pe.Objective(sense=pe.maximize, expr=obj_expr)

# Define the constraints
con_lhs_expr = sum(model.a[i] * model.x[i] for i in model.N)
con_rhs_expr = model.b 
model.con = pe.Constraint(expr=(con_lhs_expr <= con_rhs_expr))


result = solver.solve(model)

# Print the result
for i in model.N:
    print(pe.value(model.x[i]))
print(pe.value(model.obj))
