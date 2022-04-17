import os
import argparse
import re
import shutil

from auxiliares import parsear_datos_csv

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="Ruta del archivo csv", type=str, nargs="?")
parser.add_argument(
    "-c", "--corrector", help="Nombre/usuario del corrector", type=str, nargs="?"
)
parser.add_argument(
    "-a", "--actividad", help="Nombre de la actividad", type=str, required=True
)
parser.add_argument(
    "-m", "--modo", help="[A] automático, [M] manual", type=str, nargs="?", default="A"
)
parser.add_argument(
    "-e", "--estudiante", help="Nickname estudiante", type=str, nargs="?"
)
args = parser.parse_args()


# ---- Parámetros cambiables ----
# Path al archivo CSV que contiene la información de los correctores
path_csv = args.path
# Tu nombre/usuario en el archivo CSV
corrector = args.corrector
# Subdirectorio a descargar: T3, AF6, AS2 ...
actividad = args.actividad
# Estudiante (si lo hay)
estudiante = args.estudiante

# URL absoluta al repositorio, no debería ser necesario cambiarla
repo_base = r"git@github.com:IIC2233/{}.git"
path_repo = repo_base.format(actividad)


def modo_automatico():
    # Transforma el CSV a una lista de tuplas (corrector, alumno)
    datos = parsear_datos_csv(path_csv)

    # Comando inicial, crea el repositorio respectivo vacío, para poder agregarle contenido
    os.mkdir(actividad)
    os.chdir(actividad)
    os.system("git init")
    os.system("git sparse-checkout init")
    os.system(f"git remote add -f origin {path_repo}")

    my_students = ""

    # Itera sobre los alumnos y correctores, para agregar a la carpeta sólo las subcarpetas
    for linea in datos:
        alumno, corr = (linea[0], linea[1])
        if corr == corrector:
            my_students = f"{my_students} {alumno}"
    os.system(f"git sparse-checkout set {my_students}")
    os.system("git pull origin master")


def modo_manual():
    print(f"Descargando {actividad} de {estudiante}!")
    os.mkdir(actividad)
    os.chdir(actividad)
    os.system("git init")
    os.system("git sparse-checkout init")
    os.system(f"git remote add -f origin {path_repo}")
    
    os.system(f"git sparse-checkout set {estudiante}")
    os.system("git pull origin master")


def modo_forzado():

    if actividad in os.listdir():
        acepta_a_borrar_carpeta = input(
            f"Esto borrará la carpeta {actividad}/ en {os.getcwd()}/ Estás seguro?: (y/n) "
        ).lower()

        if acepta_a_borrar_carpeta == "n" or acepta_a_borrar_carpeta != "y":
            print("el modo forzado no se ejecutará. Saliendo...")
            return

        print(f"borrando carpeta {actividad} ...")
        shutil.rmtree(actividad)

    # Comando inicial, clona todo el repositorio
    print("Clonando todo el repositorio...")
    git_setup = f"git clone {path_repo}"
    os.system(git_setup)

    datos = parsear_datos_csv(path_csv)
    alumnos_del_corrector = set()

    # Itera sobre los alumnos y correctores, para extraer los alumnos a corregir
    for linea in datos:
        alumno, corr = (linea[0], linea[1])
        if corr == corrector:
            alumnos_del_corrector.add(alumno)

    # borra las carpetas de los alumnos que NO tengan que corregir
    for alumno in os.listdir(path=actividad):
        if alumno not in alumnos_del_corrector:
            shutil.rmtree(os.path.join(actividad, alumno))


if __name__ == "__main__":
    if re.search("[m]", args.modo, re.IGNORECASE):
        print("Modo manual")
        # argumentos: actividad y alumno
        assert isinstance(args.estudiante, str)
        modo_manual()

    elif re.search("[a]", args.modo, re.IGNORECASE):
        # toma las variables globales como parámetros, y descarga todos los elementos del CSV
        print("Modo automático")
        assert isinstance(args.path, str)
        assert isinstance(args.corrector, str)
        modo_automatico()

    elif re.search("[f]", args.modo, re.IGNORECASE):
        # toma las variables globales como parámetros, y descarga FORZOSAMENTE
        # los elementos del CSV

        print("Modo forzado")
        assert isinstance(args.path, str)
        assert isinstance(args.corrector, str)
        modo_forzado()

    else:
        print("ERROR: los argumentos no son correctos.")
