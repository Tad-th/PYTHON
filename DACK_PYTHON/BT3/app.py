from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('database5.db')
    return conn

with connect_db() as conn:
    conn.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        major TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Đang học'
    )
    ''')
    conn.commit()

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return render_template('index.html', students=students)


@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    major = request.form['major']
    status = request.form['status']
    
    conn = connect_db()
    
    cursor = conn.execute('SELECT * FROM students WHERE name = ? AND age = ? AND major = ?', (name, age, major))
    existing_student = cursor.fetchone()
    
    if existing_student:
        conn.close()
        return render_template('index.html', error_message="Sinh viên đã tồn tại!", students=get_all_students())
    
    conn.execute('INSERT INTO students (name, age, major, status) VALUES (?, ?, ?, ?)', (name, age, major, status))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))


@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    conn = connect_db()
    conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:student_id>')
def edit_student(student_id):
    conn = connect_db()
    cursor = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return render_template('edit.html', student=student)

@app.route('/update/<int:student_id>', methods=['POST'])
def update_student(student_id):
    name = request.form['name']
    age = request.form['age']
    major = request.form['major']
    status = request.form['status']
    conn = connect_db()
    conn.execute('''
        UPDATE students
        SET name = ?, age = ?, major = ?, status = ?
        WHERE id = ?
    ''', (name, age, major, status, student_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
def get_all_students():
    conn = connect_db()
    cursor = conn.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students


if __name__ == '__main__':
    app.run(debug=True)
