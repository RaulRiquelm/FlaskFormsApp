from flask import Flask, render_template, request

app = Flask(__name__)

# Pagina principal
@app.route('/')
def inicio():
    return render_template('index.html')

# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    resultado = None

    if request.method == 'POST':
        # Obtener los valores del formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = request.form['cantidad']

        # Realizar el cálculo
        precio_tarros= 9000
        total = int(cantidad) * precio_tarros
        descuento = 0

        if(edad >= 18 and edad <= 30):
            descuento = total * 0.15
        
        elif(edad >= 31 and edad <= 50):
            descuento = total * 0.25
        
        total_pagar = total - descuento
    

        resultado = {
            'nombre': nombre,
            'total': total,          
            'descuento': descuento,
            'total_pagar': total_pagar  
        }
    return render_template('ejercicio1.html', resultado=resultado)

#ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    
    mensaje =""

    if request.method == 'POST' :
        usuario= request.form['nombre']
        contraseña = request.form['pass']

        if usuario == "juan" and contraseña == "admin":
            mensaje = "Bienvenido administrador juan"
        
        elif usuario == "pepe" and contraseña == "user":
            mensaje = "Bienvenido usuario pepe"
        
        else:
            mensaje = "Usuario o contraseña incorrectos"
        


    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)