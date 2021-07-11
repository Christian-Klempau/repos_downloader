# repos_downloader
Permite descargar un grupo de subcarpetas de un repositorio, o bien descargar un directorio arbitrario desde cualquier carpeta.

## Modos de uso
- **automático**: descarga todas las carpetas, de los alumnos asociados a un corrector, para una actividad o tarea.

    - ejecución: `python repos_downloader.py`
    - consideraciones: líneas de `6: path_csv`, `8: corrector` y `10: actividad` deben cambiarse correctamente.



- **manual**: permite descargar el directorio de una actividad o tarea, de un alumno específico.
    - ejecución: `python repos_downloader.py "actividad" "alumno"`.
    - ejemplo: `python repos_downloader.py AF6 ChrisKlempau`


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

