from cplex import Cplex

# Problema:
# Max: 2x + 4y = z 
# Sa : x + y >= 20
#      x + y >= 10

# Crear un objeto de problema de Cplex
prob = Cplex()

# Maximizar
prob.objective.set_sense(prob.objective.sense.maximize)

# Agregar variables 'x' y 'y'
# cplex.infinity se utiliza para indicar que no hay límite superior (infinito)
prob.variables.add(names=["x", "y"],
                   obj=[3, 4],  # Coeficientes de la función objetivo
                   lb=[0, 0],  # Límites inferiores para x y y
                   ub=[prob.infinity, prob.infinity])  # Límites superiores

# Agregar restricciones
# La primera restricción: x + 2y <= 20
prob.linear_constraints.add(
    lin_expr=[[["x", "y"], [1, 2]]],
    senses=["L"],  # 'L' significa 'menor o igual que'
    rhs=[20])  # Lado derecho de la restricción

# La segunda restricción: x + y >= 10
prob.linear_constraints.add(
    lin_expr=[[["x", "y"], [1, 1]]],
    senses=["G"],  # 'G' significa 'mayor o igual que'
    rhs=[10])

# Resolver el problema
prob.solve()

# Imprimir la solución
print("Status:", prob.solution.get_status_string())
print("Valor óptimo de la función objetivo:", prob.solution.get_objective_value())
print("Valores de las variables:")
for name, value in zip(prob.variables.get_names(), prob.solution.get_values()):
    print(f"{name} = {value}")
