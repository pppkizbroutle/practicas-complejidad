import sys
import os.path
import random

def generar_certificado(archivo_entrada):
    with open(archivo_entrada, 'r') as f:
        data = f.read().splitlines()
        k = int(data[0])
        lista_vecinos = [list(map(int, x.split(','))) for x in data[1:]]

    # Iniciar con un vértice aleatorio
    vertice_actual = random.choice(range(len(lista_vecinos)))
    certificado = [vertice_actual]

    # Generar una ruta aleatoria
    while len(certificado) < k:
        vecinos = [v for v in lista_vecinos[vertice_actual] if v not in certificado]
        if not vecinos:
            break
        vertice_actual = random.choice(vecinos)
        certificado.append(vertice_actual)

    return ','.join(map(str, certificado))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("El modo de uso del programa es: python generar_certificado.py <input> <output>")

    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]

    if not os.path.isfile(archivo_entrada):
        sys.exit("No existe el archivo de entrada")

    certificado = generar_certificado(archivo_entrada)

    with open(archivo_salida, 'w') as f:
        f.write(certificado)
