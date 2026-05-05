from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'traffic_db'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM violations")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    location = request.form['location']
    count = request.form['count']
    signal = request.form['signal']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO violations (location, vehicle_count, signal_status) VALUES (%s, %s, %s)",
                (location, count, signal))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM violations WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)