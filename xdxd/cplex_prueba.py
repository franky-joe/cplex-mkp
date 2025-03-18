import cplex

# Crear un nuevo problema de CPLEX
prob = cplex.Cplex()

# Cambiar el sentido del problema a minimización
prob.objective.set_sense(prob.objective.sense.minimize)

# Añadir variables
# 'lb' es el límite inferior, 'ub' es el límite superior, 'names' son los nombres de las variables
prob.variables.add(obj=[1.0, 2.0], lb=[0.0, 0.0], ub=[40.0, cplex.infinity], names=["x1", "x2"])

# Añadir restricciones
# 'lin_expr' son las expresiones lineales, 'senses' es el sentido de las restricciones, 'rhs' es el lado derecho
prob.linear_constraints.add(
    lin_expr=[[["x1", "x2"], [1.0, 1.0]]],
    senses=["L"],
    rhs=[20.0]
)

# Resolver el problema
prob.solve()

# Mostrar la solución
print("Solution status =", prob.solution.get_status(), ":", prob.solution.status[prob.solution.get_status()])
print("Solution value  =", prob.solution.get_objective_value())
names = prob.variables.get_names()
values = prob.solution.get_values()
for name, value in zip(names, values):
    print(name, " = ", value)

