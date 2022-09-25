# BMSC_evaluacion
## Requirements
  - pipenv
el archivo server.py es el que contiene la configuracion del puerto,
debe cambiarlo si el puerto asignado esta ocupado
Se debe iniciar primeramente el entorno virtual con el siguiente comando
```sh 
evaluacion/Scripts/active
```
el siguiente comando es para ejecutar el proyecto
```sh
(evaluacion)$ flask --app server.py --debug run -p 8081
```
abrir en el navegador la direccion
127.0.0.1:8081/detalle para ver los registros de la api Toggle
o directamente en 127.0.0.1:8081 le mostrara la tabla con los datos mas importantes  
