# Aplicación de Rastreos
Proyecto Django y Django REST Framework

Instalando bibliotecas `$echo $pwd/requirements/`
``` 
# Optional
python3 -m venv .env
source .env/bin/activate
# Install
pip3 install local.txt
``` 

Python versión
``` 
python3 --version
Python 3.8.3
``` 

# PostgreSQL 14

``` 
drop database [IF EXISTS] rastreosdb with (force);
create database rastreosdb;
``` 

# Migrations
``` 
source script.sh
``` 

# Database configurations
``` 
"FILENAME": "secret.json",
"SECRET_KEY": "ak(&h5bl4pru73nei7wy!0_s++j)wy+**gtpa$dz1rdij8s***",
"DB_NAME": "rastreosdb",
"USER": "#",
"PASSWORD": "#"
``` 

# Endpoits 

- Insertar: 
`api/product/create/`

<img width="1392" alt="Captura de Pantalla 2022-05-05 a la(s) 1 01 51 p m" src="https://user-images.githubusercontent.com/56992179/166985048-e3e69dc3-70df-4252-9dd5-dc60d5f3e475.png">

- Actualizar: 
`api/product/update/<pk>/`

<img width="1392" alt="Captura de Pantalla 2022-05-05 a la(s) 1 04 55 p m" src="https://user-images.githubusercontent.com/56992179/166985491-393a3c0f-7fee-408e-bb91-34e09a8dff30.png">

- Borrar: 
`api/product/delete/<pk>/`

<img width="1392" alt="Captura de Pantalla 2022-05-05 a la(s) 1 17 18 p m" src="https://user-images.githubusercontent.com/56992179/166987611-9e4b57a4-fe02-445c-8267-c43590457f24.png">


- Detalle: 
`api/product/detail/<pk>/`

<img width="1392" alt="Captura de Pantalla 2022-05-05 a la(s) 1 16 56 p m" src="https://user-images.githubusercontent.com/56992179/166987597-25a9ab26-fcd7-453b-aabc-47726eaefbb3.png">

- Auth
Para realizar la autenticación se usaron los servicios que provee Google Firebase (Sdk de Firebase en Python), donde también se realiza para los registros

Usuario: 

<img width="1392" alt="Captura de Pantalla 2022-05-04 a la(s) 7 28 34 p m" src="https://user-images.githubusercontent.com/56992179/166991769-fa3735f2-6484-408e-9ee1-4aea30fda4da.png">

Autenticación o registro por token:  

<img width="1392" alt="Captura de Pantalla 2022-05-05 a la(s) 1 11 34 p m" src="https://user-images.githubusercontent.com/56992179/166991887-269178a2-3291-45bd-852f-ae292ff00105.png">

Permisos: 

<img width="1392" alt="Captura de Pantalla 2022-05-05 a la(s) 1 44 23 p m" src="https://user-images.githubusercontent.com/56992179/167001874-e72d883d-74bf-4e6f-a003-cb0e7f28887c.png">

Leyendo información de respaldo
``` 
python manage.py loaddata tienda_data.json
``` 

## Unit Tests
Número mínimo de carácteres

<img width="682" alt="Captura de Pantalla 2022-05-05 a la(s) 5 45 34 p m" src="https://user-images.githubusercontent.com/56992179/167037417-fe78ee86-ae00-418d-a33c-7dff8ea33362.png">





