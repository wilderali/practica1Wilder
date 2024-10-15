from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/servicios/<servicio_slug>')
def detalle_servicio(servicio_slug):
    return render_template('detalle_servicio.html', servicio_slug=servicio_slug)

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        # Aquí podrías procesar el formulario (por ejemplo, enviar un email)
        return redirect(url_for('index'))
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
