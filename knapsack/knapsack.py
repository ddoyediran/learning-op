# Import framework
import pyomo.environ as pe 
import pyomo.opt as po 

# Setting the solver
solver = po.SolverFactory('glpk') # GNU Linear Programing kit

# Solving a Knapsack problem
model = pe.ConcreteModel()


# Define the variables
model.x1 = pe.Var(domain=pe.Binary)
model.x2 = pe.Var(domain=pe.Binary)
model.x3 = pe.Var(domain=pe.Binary)
model.x4 = pe.Var(domain=pe.Binary)
model.x5 = pe.Var(domain=pe.Binary)

# define the objective function  and set the OF
obj_expr = 3 * model.x1 + 4 * model.x2 + 5 * model.x3 + 8 * model.x4 + 9 * model.x5
model.obj = pe.Objective(sense=pe.maximize, expr=obj_expr)

# Constraint expression
con_expr = 2 * model.x1 + 3 * model.x2 + 4 * model.x3 + 5 * model.x4 + 9 * model.x5 <= 20
model.con = pe.Constraint(expr=con_expr)

# Solve and postprocess
result = solver.solve(model, tee=True)

print(pe.value(model.x1)) # Get the value of var x1
print(pe.value(model.x2)) # Get the value of var x2
print(pe.value(model.x3)) # Get the value of var x3
print(pe.value(model.x4)) # Get the value of var x4
print(pe.value(model.x5)) # Get the value of var x5
print(pe.value(model.obj)) # Get the value of  the objective (Maximize) value 