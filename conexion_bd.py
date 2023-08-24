from flask import Flask, request, render_template, redirect, url_for, session
import psycopg2

app = Flask(__name__, static_folder='static')
app.secret_key = 'gesintel'

conexion_db = psycopg2.connect(
    dbname = 'scrap_config',
    user = 'scrap_config',
    password = 'QdrZ57FFcrK7gK3tIPb3',
    host = 'localhost'
)

@app.route('/')
def login():
    return render_template('login_page.html')

@app.route('/login', methods = ['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

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
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
