from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tms_secret_key'

app.config['MYSQL_HOST'] = 'mysql-1bc783e2-ks1002987-c94b.i.aivencloud.com'
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'DUMMY'
app.config['MYSQL_DB'] = 'defaultdb'
app.config['MYSQL_PORT'] = 22794

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM violations ORDER BY date_time DESC")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    vehicle_no = request.form['vehicle_no']
    owner_name = request.form['owner_name']
    phone = request.form['phone']
    violation_type = request.form['violation_type']
    fine_amount = request.form['fine_amount']
    location = request.form['location']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO violations (vehicle_no, owner_name, phone, violation_type, fine_amount, location) VALUES (%s,%s,%s,%s,%s,%s)",
                (vehicle_no, owner_name, phone, violation_type, fine_amount, location))
    mysql.connection.commit()

    # Check 3+ violations
    cur.execute("SELECT COUNT(*) FROM violations WHERE vehicle_no = %s", (vehicle_no,))
    count = cur.fetchone()[0]
    if count >= 3:
        flash(f'WARNING: {vehicle_no} ka {count} baar violation hua hai! Extra fine lagao!', 'danger')
    
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