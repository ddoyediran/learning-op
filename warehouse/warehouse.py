# Warehouse location problem 

# This is to solve an instance of the warehouse location problem. 

#import pyomo.environ as pyo
import pyomo.environ as pe 

from warehouseConcrete import create_warehouse_model

# Data set needed for this code
N = ['Stockholm', 'Solna', 'Eskiltuna'] # Warehouse location
M = ['Vasteras', 'Nykoping', 'Esk', 'Stklh'] # Customers location

# Cost of transportation from warehouse to the customers
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

P = 2

# creating the Pyomo model
model = create_warehouse_model(N, M, d, P)