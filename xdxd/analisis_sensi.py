import pulp

# Definir el problema
model = pulp.LpProblem("Maximizar_Ganancias", pulp.LpMaximize)

# Definir las variables
x_1 = pulp.LpVariable('x_1', lowBound=0)
x_2 = pulp.LpVariable('x_2', lowBound=0)

# Función objetivo original
model += 3 * x_1 + 5 * x_2, "Beneficio"

# Restricciones originales
model += 2 * x_1 + x_2 <= 20, "Restriccion1"
model += x_1 + 2 * x_2 <= 25, "Restriccion2"

# Resolver el problema original
model.solve()
print("Solución Original:")
print("x_1 = ", x_1.varValue)
print("x_2 = ", x_2.varValue)
print("Beneficio máximo:", pulp.value(model.objective))

# Cambio en el vector de costos
model.setObjective(4 * x_1 + 5 * x_2)
model.solve()
print("\nCon cambio en el vector de costos:")
print("x_1 = ", x_1.varValue)
print("x_2 = ", x_2.varValue)
print("Beneficio máximo con nuevo costo:", pulp.value(model.objective))

# Cambio en el vector del lado derecho
model.constraints["Restriccion1"].setUb(22)
model.solve()
print("\nCon cambio en el vector del lado derecho:")
print("x_1 = ", x_1.varValue)
print("x_2 = ", x_2.varValue)
print("Beneficio máximo con nueva restricción:", pulp.value(model.objective))

