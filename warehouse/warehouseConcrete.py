#import framework(s)
import pyomo.environ as pyo

def create_warehouse_model(N, M, d, P):
    model = pyo.ConcreteModel(name="(WL)") # creating the model

    # Declaring the variables
    model.x = pyo.Var(N, M, bounds=(0, 1)) # customers demands variables
    model.y = pyo.Var(N, within=pyo.Binary) # Variable to determine if the location should be built.

    # creating the Objective function
    def obj_rule(mdl):
        return sum(d[n, m] * mdl.x[n, m] for n in N for m in M)
    model.obj = pyo.Objective(rule=obj_rule)

    # Constraints
    def demand_rule(mdl, m):
        return sum(mdl.x[n, m] for n in N) == 1
    model.demand = pyo.Constraint(M, rule=demand_rule)
    
    def warehouse_active_rule(mdl, n, m):
        return mdl.x[n, m] <= mdl.y[n]
    model.warehouse_active = pyo.Constraint(N, M, rule=warehouse_active_rule)

    def num_warehouses_rule(mdl):
        return sum(mdl.y[n] for n in N) <= P
    model.num_warehouses = pyo.Constraint(rule=num_warehouses_rule)

    return model




