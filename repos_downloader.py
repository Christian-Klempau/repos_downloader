import os
import sys

# ---- Parámetros cambiables ----
# Path al archivo CSV que contiene la información de los correctores
path_csv = "datos.csv"
# Tu nombre/usuario en el archivo CSV
corrector = "Chris"
# Subdirectorio a descargar: T3, AF6, AS2 ...
actividad = "AF6"

# URL absoluta al repositorio, no debería ser necesario cambiarla
repo_base = r"https://github.com/IIC2233/"
path_repo = repo_base + actividad


def modo_automatico():
    # Transforma el CSV a una lista de tuplas (corrector, alumno)
    datos = [linea.strip().split(",") for linea in open(path_csv, "r", encoding="utf-8").readlines()]

    # Comando inicial, crea el repositorio respectivo vacío, para poder agregarle contenido
    git_setup = "git clone --depth 1 --filter=blob:none --sparse " + path_repo
    os.system(git_setup)

    # Itera sobre los alumnos y correctores, para agregar a la carpeta sólo las subcarpetas
    for linea in datos:
        alumno, corr = (linea[0], linea[1])
        if(corr == corrector):
            os.system(f"cd {actividad} && git sparse-checkout add {alumno}")


def modo_manual(actividad_especifica, alumno):
    print(f"Descargando {actividad_especifica} de {alumno}!")
    git_setup = "git clone --depth 1 --filter=blob:none --sparse " + repo_base + actividad_especifica
    os.system(git_setup)
    os.system(f"cd {actividad_especifica} && git sparse-checkout add {alumno}")


if __name__ == "__main__":
    if(len(sys.argv) == 3):
        print("Modo manual")
        # argumentos: actividad y alumno
        modo_manual(sys.argv[1], sys.argv[2])

    elif(len(sys.argv) == 1):
        # toma las variables globales como parámetros, y descarga todos los elementos del CSV
        print("Modo automático")
        modo_automatico()
    else:
        print("ERROR: los argumentos no son correctos.")
