# FlaskFormsApp

## Descripción

FlaskFormsApp es una aplicación web desarrollada con Python y Flask como parte de una evaluación académica. La aplicación cuenta con un menú principal que permite acceder a dos ejercicios independientes mediante formularios web.

El proyecto utiliza Flask para gestionar las rutas y procesar los datos ingresados por el usuario, mientras que HTML y CSS se utilizan para la interfaz gráfica.

## Funcionalidades

### Ejercicio 1: Cálculo de compra de pinturas

Permite ingresar:

* Nombre del cliente.
* Edad.
* Cantidad de tarros de pintura a comprar.

Cada tarro de pintura tiene un valor de $9.000.

Descuentos aplicados:

* Menores de 18 años: Sin descuento.
* Entre 18 y 30 años: 15% de descuento.
* Mayores de 30 años: 25% de descuento.

La aplicación muestra:

* Nombre del cliente.
* Total sin descuento.
* Monto del descuento aplicado.
* Total a pagar.

### Ejercicio 2: Validación de usuarios

La aplicación valida dos usuarios predefinidos:

| Usuario | Contraseña | Resultado                     |
| ------- | ---------- | ----------------------------- |
| juan    | admin      | Bienvenido administrador juan |
| pepe    | user       | Bienvenido usuario pepe       |

Si las credenciales son incorrectas, se muestra el mensaje:

> Usuario o contraseña incorrectos.

## Tecnologías utilizadas

* Python 3
* Flask 3.1.3
* HTML5
* CSS3
* Jinja2

## Estructura del proyecto

```text
FlaskFormsApp/
│
├── main.py
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── ejercicio1.html
│   └── ejercicio2.html
│
└── venv/
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Ingresar al proyecto

```bash
cd FlaskFormsApp
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar la aplicación

```bash
python main.py
```

La aplicación estará disponible en:

```text
http://127.0.0.1:5000
```

## Capturas de pantalla

### Menú principal

*(Agregar captura aquí)*

### Ejercicio 1

*(Agregar captura aquí)*

### Ejercicio 2

*(Agregar captura aquí)*

## Autor

**Raúl Alejandro Riquelme Gajardo**

Analista Programador | Desarrollador Full Stack

## Repositorio

Agregar aquí la URL de GitHub una vez publicado el proyecto.
