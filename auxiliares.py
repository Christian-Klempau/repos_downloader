def parsear_datos_csv(path_csv: str):
    """
    Parsea el archivo CSV, y devuelve una lista de tuplas, con los datos de cada alumno.
    Cada tupla es del tipo: (alumno, corrector)
    """

    return [
        linea.strip().split(",")
        for linea in open(path_csv, "r", encoding="utf-8").readlines()
    ]
