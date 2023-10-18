import sys
import os.path

def verificar_ruta_inducida(archivo_ejemplar, archivo_certificado):
    # Leer el ejemplar
    with open(archivo_ejemplar, 'r') as f:
        data = f.read().splitlines()
        k = int(data[0])
        lista_vecinos = [list(map(int, x.split(','))) for x in data[1:]]
    
    # Leer el certificado
    with open(archivo_certificado, 'r') as f:
        certificado = list(map(int, f.read().split(',')))

    # Verificar si la ruta es inducida
    for i in range(len(certificado) - 1):
        if certificado[i+1] not in lista_vecinos[certificado[i]]:
            return False
        for j in range(i+2, len(certificado)):
            if certificado[j] in lista_vecinos[certificado[i]]:
                return False

    # Verificar si la longitud es al menos K
    if len(certificado) < k:
        return False

    return True

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("El modo de uso del programa es: python verificar_ruta_inducida.py <input_ejemplar> <input_certificado> <output_file>")

    archivo_ejemplar = sys.argv[1]
    archivo_certificado = sys.argv[2]
    archivo_salida = sys.argv[3]

    if not os.path.isfile(archivo_ejemplar) or not os.path.isfile(archivo_certificado):
        sys.exit("Uno o ambos archivos no existen.")

    es_valido = verificar_ruta_inducida(archivo_ejemplar, archivo_certificado)

    # Salida requerida
    with open(archivo_ejemplar, 'r') as f:
        data = f.read().splitlines()
        k = int(data[0])
        S = len(data) - 1
        C = sum(len(list(map(int, x.split(',')))) for x in data[1:])

    with open(archivo_salida, "w") as f:
        f.write(f"Número de elementos en S (el conjunto universo): {S}\n")
        f.write(f"Número de subconjuntos en C: {C}\n")
        f.write(f"Valor de K: {k}\n")
        f.write(f"Respuesta a la pregunta: {'Sí' if es_valido else 'No'}\n")
