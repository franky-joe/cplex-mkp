import pulp


prob = pulp.LpProblem("MiProblema", pulp.LpMinimize)


x1 = pulp.LpVariable("x1", lowBound=0)  
x2 = pulp.LpVariable("x2", lowBound=0) 


prob += 2*x1 - x2, "Función Objetivo"


prob += (-1)*x1 + x2 <= 2, "Restricción 1"
prob +=  2*x1 + x2 <= 6, "Restricción 2"

# Especifica que CPLEX es el solucionador
solver = pulp.CPLEX_PY(msg=0)  # msg=0 para suprimir la salida de CPLEX en la consola


prob.solve(solver)


print("Estado:", pulp.LpStatus[prob.status])
print("x1 = ", x1.varValue)
print("x2 = ", x2.varValue)

