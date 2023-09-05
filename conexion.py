from flask import Flask, request, render_template, redirect, url_for, session, flash
import psycopg2

app = Flask(__name__, static_folder='static')
app.secret_key = 'gesintel'

conexion_db = psycopg2.connect(
    dbname = 'scrap_config',
    user = 'scrap_config',
    password = 'QdrZ57FFcrK7gK3tIPb3',
    host = 'localhost'
)

@app.route('/login')
def login():
    return(render_template('login_page.html'))

@app.route('/login', methods = ['POST'])
def login_post():
    username = request.form['username'].strip()
    password = request.form['password'].strip()

    cursor = conexion_db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario_nombre = %s AND usuario_clave = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()

    if user:
        session['user_id'] = user[0]
        return redirect(url_for('main_page'))
    
    else:
        return redirect(url_for('login'))
         
@app.route('/main_page')
def main_page():
    if 'user_id' in session:
        cursor = conexion_db.cursor()
        user_id = session['user_id']
        cursor.execute("SELECT usuario_nombre FROM usuarios WHERE usuario_id= %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            return render_template('main_page.html', username=user[0])
    else:
        return redirect(url_for('login'))
    
@app.route('/cambio_clave', methods=['GET', 'POST'])
def cambio_clave():
    if request.method == 'POST':
        usuario = request.form['usuario_nombre']
        antigua_clave = request.form['usuario_clave']
        nueva_clave = request.form['nueva_clave']
        confirmar_clave = request.form['confirmar_clave']

        cursor = conexion_db.cursor()
        cursor.execute["SELECT usuario_clave FROM usuarios WHERE usuario_nombre = %s", (usuario,)]
        user = cursor.fetchone()

        if user and user[0] == antigua_clave and nueva_clave == confirmar_clave:
            cursor.execute("UPDATE usuarios SET usuario_clave = %s WHERE usuario_nombre = %s", (nueva_clave, usuario)) 
            conexion_db.commit()
            cursor.close()
            return redirect(url_for('login_page'))
        
        else:
            mensaje_error = "Error en la confirmacion de la antigua clave, el nombre de usuario o la nueva clave"
            return render_template('cambio_clave.html', mensaje_error=mensaje_error)
        
    return render_template('cambio_clave.html')
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/mantenedor_proyecto')
def mantenedor_page():
    if 'user_id' in session:
        cursor = conexion_db.cursor()
        user_id = session['user_id']
        cursor.execute("SELECT usuario_nombre FROM usuarios WHERE usuario_id= %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            return render_template('mantenedor_proyecto.html', username=user[0])
    else:
        return redirect(url_for('login'))     



@app.route('/mantenedor_proyecto', methods= ['GET'])
def obtener_registro_bd():
    cursor = conexion_db.cursor()
    cursor.execute('SELECT * from proyectos')
    data = cursor.fetchall()
    return render_template('mantenedor_proyecto.html', proyectos = data)



@app.route('/add_proyecto', methods =['POST'])
def agregar_proyecto():
    if request.method == "POST":
        proyecto_descrip = request.form['proyecto_descrip']
        cursor = conexion_db.cursor()
        cursor.execute('INSERT INTO proyectos (proyecto_descrip) VALUES (%s)', (proyecto_descrip,) )
        conexion_db.commit()
        cursor.close()

    flash('Se agrego correctamente el Proyecto')
    return render_template("mantenedor_proyecto.html")

if __name__ == '__main__':
    app.run(debug=True)
