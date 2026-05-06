from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('traffic.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS traffic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            vehicle_count INTEGER,
            signal_status TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('traffic.db')
    c = conn.cursor()
    c.execute("SELECT * FROM traffic")
    data = c.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    location = request.form['location']
    count = request.form['count']
    signal = request.form['signal']

    conn = sqlite3.connect('traffic.db')
    c = conn.cursor()
    c.execute("INSERT INTO traffic (location, vehicle_count, signal_status) VALUES (?, ?, ?)",
              (location, count, signal))
    conn.commit()
    conn.close()

    return redirect('/')

app.run(debug=True)
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('traffic.db')
    c = conn.cursor()
    c.execute("DELETE FROM traffic WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')