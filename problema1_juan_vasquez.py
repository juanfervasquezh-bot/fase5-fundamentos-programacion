# Estudiante: Juan Vasquez
# Grupo: 119
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Problema 1: Clasificación del nivel de compromiso de clientes

# Matriz de datos: [ID del cliente, duración de sesión, número de clics]
sesiones = [
    [101, 220, 12],
    [102, 45, 5],
    [103, 150, 6],
    [104, 200, 4],
    [105, 90, 2]
]

# Función para clasificar el nivel de compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Programa principal
print("======================================")
print("   INFORME DE COMPROMISO DE CLIENTES")
print("======================================")

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    nivel = clasificar_compromiso(duracion, clics)

    print(f"Cliente: {id_cliente}")
    print(f"Duración de la sesión: {duracion} segundos")
    print(f"Número de clics: {clics}")
    print(f"Nivel de compromiso: {nivel}")
    print("--------------------------------------")