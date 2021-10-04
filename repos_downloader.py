import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="Ruta del archivo csv", type=str, nargs='?')
parser.add_argument(
    "-c", "--corrector", help="Nombre/usuario del corrector", type=str, nargs='?'
)
parser.add_argument("-a", "--actividad", help="Nombre de la actividad", type=str, required=True)
parser.add_argument(
    "-m", "--modo", help="[A] automático, [M] manual", type=str, nargs='?', default="A"
)
parser.add_argument("-e", "--estudiante", help="Nickname estudiante", type=str, nargs='?')
args = parser.parse_args()


# ---- Parámetros cambiables ----
# Path al archivo CSV que contiene la información de los correctores
path_csv = args.path
# Tu nombre/usuario en el archivo CSV
corrector = args.corrector
# Subdirectorio a descargar: T3, AF6, AS2 ...
actividad = args.actividad

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
    if(re.search("[m]", args.modo, re.IGNORECASE)):
        print("Modo manual")
        # argumentos: actividad y alumno
        assert isinstance(args.estudiante, str)
        modo_manual(args.actividad, args.estudiante)

    elif(re.search("[a]", args.modo, re.IGNORECASE)):
        # toma las variables globales como parámetros, y descarga todos los elementos del CSV
        print("Modo automático")
        assert isinstance(args.path, str)
        assert isinstance(args.corrector, str)
        modo_automatico()
    else:
        print("ERROR: los argumentos no son correctos.")
