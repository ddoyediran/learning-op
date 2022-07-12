# Import framework
import pyomo.environ as pe 
import pyomo.opt as po 

# Setting the solver
solver = po.SolverFactory('glpk') # GNU Linear Programing kit

# Solving a Knapsack problem
model = pe.ConcreteModel()

# Set of items
model.N = pe.RangeSet(1, 5) 

c = {1: 3, 2: 4, 3 : 5, 4 : 8, 5 : 9} # Cost 
a = {1 : 2, 2 : 3, 3 : 4, 4 : 5, 5 : 9} # size
b = 20

# print(set(model.N))