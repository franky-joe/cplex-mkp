import sys
from io import StringIO
import cplex 
def save_help_to_file(cls, filename):
    # Redirigir la salida de help a un objeto StringIO
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        help(cls)
        # Obtener el contenido de StringIO
        help_output = sys.stdout.getvalue()
    finally:
        # Restaurar sys.stdout
        sys.stdout = old_stdout
    
    # Escribir el contenido en un archivo
    with open(filename, 'w') as f:
        f.write(help_output)

prob = cplex.Cplex()

save_help_to_file(prob.parameters, 'help_parameters.txt')
