# repos_downloader
Permite descargar un grupo de subcarpetas de un repositorio, o bien descargar un directorio arbitrario desde cualquier carpeta.

## Modos de uso
- **automático**: descarga todas las carpetas, de los alumnos asociados a un corrector, para una actividad o tarea.

    - ejecución: `python repos_downloader.py -p AF3.csv -c 'Chris Klempau' -a AF3`
    - argumentos: 
         - `-a = NOMBRE_ACTIVIDAD`
         - `-c = NOMBRE_CORRECTOR` (según csv y tipo `str`)
         - `-p = PATH_CSV`



- **manual**: descarga una actividad/tarea específica de algún alumne.

    - ejecución: `python repos_downloader.py -m M -e {alumne} -a {actividad}` donde alumne es el usuario GitHub correspondiente, y actividad es `AFx, ASx, Tx`.


Ojo: las descargas siempre se harán en `nombre_actividad/`, por ejemplo `T2/`, a partir de la ubicación del archivo _python_. **La carpeta NO debe existir antes**. 
Por ejemplo, antes de una ejecución de **automático** el directorio se vería así:

```
/
├── datos.csv
└── repos_downloader.py
```
Y después:
```
/
├── AF6
│   ├── Alumno1
│   │   ├── archivo1
│   │   ├── archivo2
│   ├── Alumno2
│   │   ├── archivo1
│   │   ├── archivo2
│   │   ├── archivo3
│   ├── Alumno3
│   │   ├── archivo1
├── datos.csv
└── repos_downloader.py
```

El archivo `.csv`, debiera verse algo así:

```
GithubAlumno,Corrector
alumno1,corrector1
alumno2,corrector1
alumno3,corrector1
alumno1,corrector2
alumno1,corrector3
alumno2,corrector3
.
.
.
```

### Posibles errores:

Error de consola: `failed to initialize sparce-checkout`
Se debe a tener una versión de `git` antigua. Se actualiza con:

```
Windows: git update-git-for-windows
MacOS: brew upgrade git
Linux: sudo apt-get install git
```