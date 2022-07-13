"""
source: https://github.com/brentertainer/pyomo-tutorials/blob/master/introduction/02-lp-pyomo.ipynb
Problem Statement
Exercise 2.12 from Operations Research: Models and Methods by Jensen & Bard

Ten jobs are to be completed by three workers during the next week. Each worker has a 40-hour work week. 
The times for the workers to complete the jobs are shown in the table. The values in the cells assume that 
each job is completed by a single worker; however, jobs can be shared, with completion times being determined 
proportionally If no entry exists in a particular cell, it means that the corresponding job cannot be performed 
by the corresponding worker. Set up and solve an LP model that will determine the optimal assignment of workers to jobs. 
The goal is to minimize the total time required to complete all the jobs.

Data:

Workers \ Tasks	1	2	3	4	5	6	7	8	9	10
A	            -	7	3	-	-	18	13	6	-	9
B	            12	5	-	12	4	22	-	17	13	-
C	            18	-	6	8	10	-	19	-	8	15

"""

# Import package
import pyomo.environ as pe 
import pyomo.opt as po 
import pandas as pd 

# Define the data 
workers = {"A", "B", "C"} # number of workers
tasks = set(range(1, 11)) # Number of available tasks

# Hours each worker can work on each task - no data means worker can't work in that hour.
c = {
    ("A", 2): 7,
    ("A", 3): 3,
    ("A", 6): 18,
    ("A", 7): 13,
    ("A", 8): 6,
    ("A", 10): 9,
    ("B", 1): 12,
    ("B", 2): 5,
    ("B", 4): 12,
    ("B", 5): 4,
    ("B", 6): 22,
    ("B", 8): 17,
    ("B", 9): 13,
    ("C", 1): 18,
    ("C", 3): 6,
    ("C", 4): 8,
    ("C", 5): 10,
    ("C", 7): 19,
    ("C", 9): 8,
    ("C", 10): 15,
}

max_hours = 40 # maximum hour that each worker can work per week

# Developing the model
model = pe.ConcreteModel() # create the model

# Define the set
model.workers = pe.Set(initialize=workers) # Set of workers
model.taks = pe.Set(initialize=tasks) # Set of tasks

# Dfine the parameters
model.c = pe.Param(model.workers, model.tasks, initialize=c, default=1000) # hours workers can complete tasks
model.max_hours = pe.Param(initialize=max_hours) # maximum hours each workers can work per week


# define the decision variables
model.x = pe.Var(model.workers, model.tasks, domain=pe.Reals , bounds=(0,1))

# Set the constraints
expr = sum(model.c[w, t] * model.x[w, t] for w in model.workers for t in model.tasks)
model.objective = pe.Objective(sense=pe.minimize, expr=expr)

# maximum task done iat each time should be less than or equal to 1
model.tasks_done = pe.ConstraintList()
for t in model.tasks:
    lhs = sum(model.x[w, t] for w in model.workers)
    rhs = 1
    model.tasks_done.add(lhs <= rhs)

# Maximum hours each worker can work
model.hour_limit = pe.ConstraintList()
for w in model.workers:
    lhs = sum(model.c[w, t] * model.x[w, t] for t in model.tasks)
    rhs = model.max_hours
    model.hour_limit.add(lhs <= rhs)



# solver = 
