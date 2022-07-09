# Warehouse location problem 

#import pyomo.environ as pyo
import pyomo.environ as pe 
import pyomo.opt as po 

N = ['Stockholm', 'Solna', 'Eskiltuna'] # Warehouse location
M = ['Vastras', 'Nykoping', 'Esk', 'Stklh'] # Customers location