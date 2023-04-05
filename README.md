# Desarrollador Python -> Prueba Técnica

Micro-servicio para la tabla *Employee* el cual es capaz de insertar, actualizar, borrar y consultar (CRUD) información utilizando el FrameWork de Django y haciendo uso de PostgreSQL. 

## Instrucción de uso: 

*Nota*: Antes de seguir con las instrucciones es necesario tener instalado:

- Docker
- Docker-compose


1. Clone el proyecto:  

```sh
git clone https://github.com/JeissonArcadio778/prueba-cobrando-bpo.git
```

2. Instale módulos:

```sh
pip install -r requirements.txt
```

3. Uso de Docker-compose: 

```sh
docker-compose up
```

## Probar funcionamiento: 

Este microservicio está compuesto por rutas que sirven distintos tipos Métodos para la gestión de *Employees*. 

### Endpoints - Methods:

    Employee

- Crear empleado --> *POST*: `http://localhost:1234/employee`

- Listar empleados --> *GET*: `http://localhost:1234/employee `

- Buscar empleado por idCode --> *GET*: `http://localhost:1234/employee/<idCode> `

- Actualizar información empleado --> *PUT*: `http://localhost:1234/employee/<idCode>`

- Eliminar empleado --> *DELETE*: `http://localhost:1234/employee/<idCode> `

### 

    Departments

- Crear departamento --> *POST*: `http://localhost:1234/departments`

- Listar departamentos --> *GET* `http://localhost:1234/departments `

- Buscar departamentos por idCode --> *GET*: `http://localhost:1234/departments/<idCode> `

- Actualizar información departamento --> *PUT*: `http://localhost:1234/departments/<idCode> `

- Eliminar departamento --> *DELETE* `http://localhost:1234/departments/<idCode> `

## POSTMAN: Ejemplos de Uso

Aqui iran los ejemplos hechos con postman.


Hecho por: 