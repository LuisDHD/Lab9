"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    
    if codigos[medio] == objetivo:
        return medio
    elif codigos[medio] < objetivo:
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)
    else:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)


#1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?   Éxito: Cuando el elemento en la posición central (codigos[medio]) es exactamente igual al objetivo. En ese caso retorna el índice medio.Fracaso (Intervalo vacío): Cuando el índice izquierda se vuelve mayor que el índice derecha (izquierda > derecha). Esto significa que ya no quedan elementos por revisar y el objetivo no existe en la lista (retorna -1).
#2. ¿Por qué no debes incluir nuevamente la posición central en el siguiente intervalo?
#Porque ya comprobaste en la llamada actual que el valor en la posición central no es el objetivo. Si lo incluyeras de nuevo (ej. pasando medio en lugar de medio + 1 o medio - 1), correrías el riesgo de entrar en un ciclo infinito cuando el intervalo se reduzca a uno o dos elementos.
#3. Completa la traza buscando 300 en codigos.
# 
# 
# 
#   Llamada | Izquierda | Derecha | Medio | Decisión
#   --------|-----------|---------|-------|-----------------------
#      1    |     0     |    6    |   3   | 415 > 300 -> Izquierda
#      2    |     0     |    2    |   1   | 205 < 300 -> Derecha
#      3    |     2     |    2    |   2   | 310 > 300 -> Izquierda
#      4    |     2     |    1    |   -   | Termina (-1)

# 4. 4. ¿Qué diferencia hay entre el progreso de esta función y el de contar_desde_limite()?   
#La función anterior (contar_desde_limite) tiene un progreso lineal: en cada llamada recursiva reduce el problema en un solo elemento (i + 1).
#Esta función (buscar_codigo) tiene un progreso logarítmico: en cada llamada recursiva descarta la mitad completa del arreglo restante, haciendo que la búsqueda sea drásticamente más rápida en listas grandes.
#
#


if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                      # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0
