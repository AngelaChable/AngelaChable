import random

def generar_calificaciones(num_alumnos, num_materias):
    calificaciones = []
    for _ in range(num_materias):
        fila = [random.randint(0, 100) for _ in range(num_alumnos)]
        calificaciones.append(fila)
    return calificaciones

def imprimir_matriz(calificaciones):
    num_alumnos = len(calificaciones[0])
    num_materias = len(calificaciones)

    encabezado_alumnos = " " * 9  
    for i in range(1, num_alumnos + 1):
        encabezado_alumnos += f"Alumno {i:2} "
    print(encabezado_alumnos)

   
    for i, fila in enumerate(calificaciones):
        fila_str = f"Materia {i+1:2}: "
        for calif in fila:
            fila_str += f"{calif:7} "
        print(fila_str)


def buscar_calificacion(calificaciones, alumno, materia):
    return calificaciones[materia - 1][alumno - 1]

calificaciones = generar_calificaciones(100, 5)


print("Matriz completa de calificaciones:")
imprimir_matriz(calificaciones)


alumno_buscado = int(input("\nIngrese el número de alumno a buscar (1-100): "))
materia_buscada = int(input("Ingrese el número de materia a buscar (1-5): "))

if 1 <= alumno_buscado <= 100 and 1 <= materia_buscada <= 5:
    calificacion_buscada = buscar_calificacion(calificaciones, alumno_buscado, materia_buscada)
    print(f"\nLa calificación del alumno {alumno_buscado} en la materia {materia_buscada} es: {calificacion_buscada}")
else:
    print("Los números de alumno y materia deben estar entre 1 y 100.")
