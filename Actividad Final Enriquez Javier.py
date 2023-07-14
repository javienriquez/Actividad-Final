def menu():
    print("Menú")
    print("a) Mostrar la lista por orden alfabética de los de Alumnos. ")
    print("b) Mostrar la lista ordenada de alumnos con sus notas. ")
    print("c) Mostrar la lista de alumnos con sus promedios. ")
    print("d) Mostrar la nota media de los alumnos. ")
    print("e) Mostras la nota media de los alumnos aprobados. ")
    print("f) Mostrar la nota media de los alumnos suspendidos. ")
    print("g) Salir del Programa. ")
    opcion = input("Elija una opción. ")
    return opcion.lower()

def lista_ordenada_alumnos(alumnos):
    for alumno in sorted(alumnos):
        print(alumno)

def lista_alumnos_notas(alumnos):
    for alumno in sorted(alumnos):
        notas = alumnos[alumno]
        print(f"{alumno}: {notas}") 


def lista_alumnos_promedio(alumnos):
    for alumno in sorted(alumnos):
     notas = alumnos[alumno]
     promedio = sum(notas) / len(notas)
     print(f"{alumno}: promedio: {round(promedio, 2)}")


def nota_media_alumnos(alumnos):
    todas_las_notas = []
    for notas in alumnos.values():
        todas_las_notas.extend(notas)
        promedio_notas = sum(todas_las_notas) / len(todas_las_notas)
        print(f"El promedio de las notas es {round(promedio_notas, 2)}.")


def nota_media_alumnos_aprobados(alumnos):
    notas_alumnos_aprobados = []
    for notas in alumnos.values():
        promedio = sum(notas) / len(notas)
        if promedio >= 7:
            notas_alumnos_aprobados.append(promedio)
    if notas_alumnos_aprobados:
        promedio_notas_aprobadas = sum(notas_alumnos_aprobados) / len(notas_alumnos_aprobados)
        print(f"El promedio de las notas de alumnos aprobados es {round(promedio_notas_aprobadas, 2)}.")
    else:
        print("No hay alumnos aprobados.")


def nota_media_alumnos_suspendidos(alumnos):
    notas_alumnos_suspendidos = []
    for notas in alumnos.values():
        promedio = sum(notas) / len(notas)
        if promedio <= 6:
            notas_alumnos_suspendidos.append(promedio)
    if notas_alumnos_suspendidos:
        promedio_notas_suspendidos = sum(notas_alumnos_suspendidos) / len(notas_alumnos_suspendidos)
        print(f"El promedio de las notas de los alumnos suspendidos es {round(promedio_notas_suspendidos, 2)}.")
    else:
        print("No hay alumnos suspendidos.")





print("cargue las notas de los alumnos")
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos que desee cargar notas: "))
alumnos = {}
for i in range(cantidad_alumnos):
    notas = []

    nombre_alumno = input("Ingrese el nombre del alumno: ")
    cantidad_notas = int(input("Ingrese la cantidad de notas, entre 3 y 6: "))

    while cantidad_notas < 3 or cantidad_notas > 6:
        print("Debe ingresar entre 3 y 6 notas.")
        cantidad_notas = int(input("Ingrese la cantidad de notas. entre 3 y 6: "))
    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)

    alumnos[nombre_alumno] = notas



opcion = menu()
while opcion != "g":
    if opcion == "a":
        print("Menú")
        print("Lista ordenada de alumnos")
        lista_ordenada_alumnos(alumnos)
    elif opcion == "b":
        
        print("Lista ordenada de alumnos con las notas")
        lista_alumnos_notas(alumnos)
    elif opcion == "c":
        
        print("Lista ordenada de promedios de alumnos")
        lista_alumnos_promedio(alumnos)
    elif opcion == "d":
        
        print("Notas promedio")
        nota_media_alumnos(alumnos)
    elif opcion == "e":
        
        print("Promedio de notas de alumnos aprobados")
        nota_media_alumnos_aprobados(alumnos)
    elif opcion == "f":
        
        print("Promedio de notas de alumnos desaprobados")
        nota_media_alumnos_suspendidos(alumnos)
    else:
        print("Opcion inválida. Elija una opción válida")
    opcion = menu()
    
print("Usted ha salido del programa.")


