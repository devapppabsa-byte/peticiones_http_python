from flask import Flask, render_template, request

aplicacion = Flask(__name__)



@aplicacion.route('/')
def form():
    return render_template('form.html')


@aplicacion.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form['nombre']
    edad = request.form['edad']
    correo = request.form['correo']

    return render_template('result.html', nombre=nombre, edad=edad, correo=correo)


if __name__ == '__main__':
    aplicacion.run(debug=True)