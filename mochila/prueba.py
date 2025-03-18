from cplex import Cplex

def simple_cplex_example():
    # Crear una instancia de un problema de optimización
    problem = Cplex()

    # Configurar el problema como un problema de minimización
    problem.objective.set_sense(problem.objective.sense.minimize)

    # Agregar variables al problema con un límite inferior de 0 y un límite superior de 10
    names = ["x1", "x2", "x3"]
    lower_bounds = [0, 0, 0]
    upper_bounds = [10, 10, 10]
    objective_coefficients = [1, 2, 3]
    
    problem.variables.add(obj=objective_coefficients,
                          lb=lower_bounds, ub=upper_bounds,
                          names=names)

    # Definir las restricciones del problema
    # x1 + x2 + x3 <= 20
    constraint = [["x1", "x2", "x3"], [1.0, 1.0, 1.0]]
    problem.linear_constraints.add(lin_expr=[constraint],
                                   senses=["L"],
                                   rhs=[20])

    # Resolver el problema
    problem.solve()

    # Imprimir la solución
    print("Solution status =", problem.solution.get_status())
    print("Solution value =", problem.solution.get_objective_value())
    var_names = problem.variables.get_names()
    var_values = problem.solution.get_values()
    for name, value in zip(var_names, var_values):
        print(name, "=", value)

if __name__ == "__main__":
    simple_cplex_example()

