import cplex
from inputdata import read_mkp_data

class MKsolver:
    def __init__(self):
        # Cplex
        self.prob = cplex.Cplex()
        self.prob.objective.set_sense(self.prob.objective.sense.maximize)

        # Datos basicos mochila
        self.beneficios = None
        self.Matriz_pesos = None
        self.capacidades = None
        self.ndimenciones = None
        self.nobjetos = None

        # Datos para cplex
        self.tiempo_limite =  None
        self.gap = None

        # Datos Salida
        self.valor_optimo = None
        self.tiempo_solucion = None
        self.gap_solucion = None
        self.cota_inferior = None
        self.cota_superior = None
        self.estado_solucion = None

        # Paths


    def set_problem(self, path_archivo, tiempo_limite, gap):
        mochila = read_mkp_data(path_archivo) # Toma el problema desde el archivo 
        self.beneficios = mochila[0]
        self.capacidades = mochila[1]
        self.Matriz_pesos = mochila[2]
        self.ndimenciones = len(self.capacidades)
        self.nobjetos = len(self.beneficios)

        # Set cplex parameters
        self.prob.parameters.timelimit.set(tiempo_limite)
        self.prob.parameters.mip.tolerances.mipgap.set(gap)

    def add_var_binarias(self):
        self.var_names = ["x{}".format(i) for i in range(self.nobjetos)]
        var_types = [self.prob.variables.type.binary] * self.nobjetos
        self.prob.variables.add(names=self.var_names, types=var_types, obj=self.beneficios)


    def add_restricciones(self):
        for d in range(self.ndimenciones):
            restriccion = [["x{}".format(i) for i in range(self.nobjetos)], self.Matriz_pesos[d]]
            self.prob.linear_constraints.add(
                lin_expr=[restriccion],
                senses=["L"],
                rhs=[self.capacidades[d]]
                )

    def solve(self):
        tiempo_inicio = self.prob.get_time()
        self.prob.solve()
        # Calcular y guardar tiempo de solucion
        self.tiempo_solucion = self.prob.get_time() - tiempo_inicio 

        # Obtener datos de la solucion
        self.obj_value = self.prob.solution.get_objective_value()
        self.gap_solucion = self.prob.solution.MIP.get_mip_relative_gap()
        self.cota_inferior = self.obj_value
        self.cota_superior = self.prob.solution.MIP.get_best_objective()
        self.estado_solucion = self.prob.solution.get_status_string()
    
    
    def mostrar_solucion(self):
        print(f"Objetivo = {self.obj_value}")
        print(f"Estado de la solucion = {self.estado_solucion}")
        print(f"Tiempo de solucion = {self.tiempo_solucion}")
        print(f"Gap = {self.gap_solucion}")
        print(f"Cota inferior = {self.cota_inferior}")
        print(f"Cota superior = {self.cota_superior}")
        for j in range(self.nobjetos):
            valor_variable = self.prob.solution.get_values(f'x{j}')
            print(f"Variable x{j} = {valor_variable}")
    
# Ejemplo de uso
if __name__ == "__main__":
    solver = MKsolver()
    path_archivo = "mochila_multidimencional/datos/gk06.dat"
    tiempo_limite = 30 # Segundos
    gap = 0.0 # Tolerancia 
    
    solver.set_problem(path_archivo, tiempo_limite, gap)
    solver.add_var_binarias()
    solver.add_restricciones()

    # Escribe el problema(no la solucin) en un archivo
    solver.prob.write("mochila.lp")

    # Para tener mas informasion sobre la solucion del problema revisar los metodos write de la clase prob.solution

    solver.solve()
    solver.mostrar_solucion()