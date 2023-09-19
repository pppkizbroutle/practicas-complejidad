"""
Práctica 2: Esquemas de Codificación

Integrantes:
- Erik Rangel Limón
- Axel Ducloux Hurtado
- Alejandro Terrazas Rivera
"""
# Paquetería para leer los argumentos con los que fue llamado el
# programa:
import sys
# Paquetería para verificar si un archivo existe:
import os.path

"""
Clase Matriz que genera una matriz de adyacencias dada una cadena de
entrada que debe seguir el esquema de codificación que propusimos.
Elegimos un esquema de codificación que utiliza listas de vecindades
"""
class Matrix:

    """
    Función constructor que recibe el esquema de codificación como
    parámetro.
    """
    def __init__(self, e):
        try:
            k, m, n, e = self.decode(e)
            self.k = k
            self.m = m
            self.n = n
            self.e = e
        except:
            print("No es una codificación válida")
    
    """
    Función que decodifica la cadena de texto recibida como parámetro,
    y crea la matriz de adyacencias correspondiente.
    """
    def decode(self, glv):
        l = glv.splitlines()
        k = int(l[0])
        n = len(l) - 1
        m = [0] * n
        for row in range(len(m)):
            m[row] = [0] * n
        e = 0
        i = 1
        while i <= n:
            v = l[i].split(",")
            for neigh in v:
                e = e + 1
                j = int(neigh)
                m[i-1][j] = 1
            i = i + 1
        return k, m, n, e//2

    """
    Función que dado un número, nos regresa su cadena en binario
    """
    def dec_to_bin(self, k):
        if k == 0:
            return "0"
        n = k
        r = ""
        while n >= 1:
            if n % 2 == 1:
                r = "1" + r
            else:
                r = "0" + r
            n = n // 2
        return r

    """
    Método para convertir nuestra matriz de adyacencias a un esquema
    de codificación que utiliza únicamente el lenguaje binario.
    """
    def __str__(self):
        r = ""
        i = 0
        while i < self.n:
            r = r + "10"
            j = 0
            while j < self.n:
                if self.m[i][j] == 0:
                    r = r + "00"
                else:
                    r = r + "01"
                j = j + 1
            i = i + 1
        r = r + "11" + self.dec_to_bin(self.k)
        return r

# Los argumentos del programa
args = sys.argv

# Si el número de argumentos no son los correctos, mandamos un mensaje
# con el modo de uso.
if len(args) != 3:
    sys.exit("El modo de uso del programa es: python esquemas.py <input> <output>")

entrada = args[1]
salida = args[2]

# Verificamos si el primer argumento es un archivo existente
if not os.path.isfile(entrada):
    sys.exit("No existe el archivo")

# Leemos el archivo
with open(entrada, "r") as file:
    e = file.read()
    # Creamos la matriz de adyacencias
    matrix = Matrix(e)
    # Imprimimos su información
    print(f'La gráfica tiene {matrix.n} vértices y {matrix.e} aristas')
    print(f'El valor de K es {matrix.k}')
    archivo = open(salida, "w")
    # Escribimos el archivo de salida con el esquema de codificación
    # en binario
    archivo.write(str(matrix))
    archivo.close()
