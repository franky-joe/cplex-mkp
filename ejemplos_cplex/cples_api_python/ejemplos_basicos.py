import cplex 

"""
#Problema 1

Maximizar
  x1 + 2*x2 + 3*x3
Sujeto a
  -x1 + x2 + x3 <= 20
  x1 - 3*x2 + x3 >= 30
Con estos límites
  5 <= x1 <= 40
  0 <= x2 <= infinito
  0 <= x3 <= infinito
"""
prob = cplex.Cplex()
prob.objective.set_sense(prob.objective.sense.maximize)

# Definicion de variables
prob.variables.add(
    names=["x1", "x2", "x3"],                       # Nombres para las variables
    types=["C", "C", "C"],                          # Tipo de variables (continuas)
    obj=[1,2,3],                                    # Coeficientes funcion objetivo
    lb=[5,0,0],                                     # Cota inferir variables
    ub=[40, cplex.infinity, cplex.infinity]         # Cota superior variables 
)
# Los tipos de variables son C (continuas), B (binarias) e I (enteras)

# Definicion de restricciones
prob.linear_constraints.add(
    lin_expr=[[[ "x1", "x2", "x3"], [-1, 1, 1]],    # Coeficienes de las variables en la primera restriccion
              [[ "x1", "x2", "x3"], [1, -3, 1]]],   # Coeficienes de las variables en la segunda restriccion
    senses = ["L", "G"],                            # Menor o igual y Mayor o igual, respectivamente
    rhs = [20, 30]                                  # Lado derecho de la restriccion
)
# L es menor o igual, G es mayor o igual, E es igual, R es rango

prob.solve()

print(f"Valor óptimo: {prob.solution.get_objective_value()}")
print(f"Variables: {prob.solution.get_values()}")  



"""
# Problema 2

Maximizar
  3*x1 + 4*x2
Sujeto a
  2*x1 + 3*x2 <= 12.5
  x1 - x2 >= 2.5
Con estos límites
  0 <= x1 <= infinito
  0 <= x2 <= infinito
"""
prob2 = cplex.Cplex()

# Objetivo 
prob2.objective.set_sense(prob2.objective.sense.maximize)
# Variables
prob2.variables.add(
    names = ['x1','x2'],
    types= ["I", "I"],
    obj = [3, 4],
    lb = [0,0],
    ub=[cplex.infinity, cplex.infinity])

# Restricciones
prob2.linear_constraints.add(
    lin_expr=[[['x1','x2'], [2,3]],
              [['x1','x2'], [1,-1]]],
    senses=['L','G'],
    rhs = [12.5, 2.5]
)


# Resolver
prob2.solve()
print(f"Valor óptimo: {prob2.solution.get_objective_value()}")
print(f"Variables: {prob2.solution.get_values()}")

# Problema tipo Mochila 

# Crear el problema
prob3 = cplex.Cplex()

# Establecer el sentido del objetivo
prob3.objective.set_sense(prob3.objective.sense.maximize)

# Agregar variables
prob3.variables.add(
    names=['x1', 'x2', 'x3', 'x4', 'x5'],
    types=['B', 'B', 'B', 'B', 'B'],
    obj=[4, 2, 10, 1, 2],
)

# Agregar restricciones
prob3.linear_constraints.add(
    lin_expr=[
        [['x1', 'x2', 'x3', 'x4', 'x5'], [14, 1, 4, 1, 2]],
        [['x1', 'x2', 'x3', 'x4', 'x5'], [3, 12, 5, 4, 3]]
    ],
    senses=['L', 'L'],
    rhs=[15, 13]
)

# Resolver el problema
prob3.solve()

# Imprimir el valor óptimo y los valores de las variables
print(f"Valor óptimo: {prob3.solution.get_objective_value()}")
print(f"Variables: {prob3.solution.get_values()}")
