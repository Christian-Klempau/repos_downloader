# repos_downloader
Permite descargar un grupo de subcarpetas de un repositorio, o bien descargar un directorio arbitrario desde cualquier carpeta.

- `python repos_downloader.py -h`: despliega información útil sobre el modo de uso.

## Modos de uso
- **automático**: descarga todas las carpetas, de los alumnos asociados a un corrector, para una actividad o tarea.

    - ejecución: `python repos_downloader.py -p AF3.csv -c 'Chris Klempau' -a AF3`
    - argumentos: 
         - `-a = NOMBRE_ACTIVIDAD`
         - `-c = NOMBRE_CORRECTOR` (según csv y tipo `str`)
         - `-p = PATH_CSV`
  
<br>

- **forzado**: funciona igual que automático, solo que asegura el funcionamiento del script al no usar `git-sparse`. Es algo más lento. Debes agregar el flag `-m F` al llamar al script.
    - - ejecución: `python repos_downloader.py -p AF3.csv -c 'Chris Klempau' -a AF3 -m F`

<br>

- **manual**: descarga una actividad/tarea específica de algún alumne.

    - ejecución: `python repos_downloader.py -m M -e {alumne} -a {actividad}` donde alumne es el usuario GitHub correspondiente, y actividad es `AFx, ASx, Tx`.

## Consideraciones
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

### Posibles errores

Error de consola: `failed to initialize sparce-checkout`
Se debe a tener una versión de `git` antigua. Se actualiza con:

```
Windows: git update-git-for-windows
MacOS: brew upgrade git
Linux: sudo apt-get install git
```

Si a pesar de lo anterior no te funciona, trata de utilizar el **modo forzado** para descargar las carpetas.

Si el script tiene problemas encontrando tu nombre en el csv, prueba escribiendo el corrector sin cremillas, es decir: `ChrisKlempau` en vez de `'ChrisKlempau'`. Ojo que si tu nombre tiene espacios las cremillas **deberían** ser necesarias.