# Warehouse location problem 

# This is to solve an instance of the warehouse location problem. 

import pyomo.environ as pyo 

from warehouseConcrete import create_warehouse_model

# Data set needed for this code
N = ['Stockholm', 'Solna', 'Eskiltuna'] # Warehouse location
M = ['Vasteras', 'Nykoping', 'Esk', 'Stklh'] # Customers location

# Cost associated with serving each customers from the warehouse
d = {
    ('Stockholm', 'Vasteras'): 1956,
    ('Stockholm', 'Nykoping'): 1606,
    ('Stockholm', 'Esk'): 1410,
    ('Stockholm', 'Stklh'): 330,
    ('Solna', 'Vasteras'): 1069,
    ('Solna', 'Nykoping'): 1792,
    ('Solna', 'Esk'): 531,
    ('Solna', 'Stklh'): 567,
    ('Eskiltuna', 'Vasteras'): 485,
    ('Eskiltuna', 'Nykoping'): 2322,
    ('Eskiltuna', 'Esk'): 324,
    ('Eskiltuna', 'Stklh'): 1236,
}

P = 2 # Number of warehouses needed

# creating the Pyomo model
model = create_warehouse_model(N, M, d, P)

# creating the solver interface and solve the model
solver = pyo.SolverFactory('glpk')
res = solver.solve(model)

# check if the result is optimal and if the status is ok
pyo.assert_optimal_termination(res) 

# Print the optimal warehouse locations
model.y.pprint()