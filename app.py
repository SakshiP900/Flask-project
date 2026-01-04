from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# Database connection using environment variables (from K8s Secret)
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

# Home page
@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)

# Add student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        return redirect('/')
    return render_template('add.html')

# Delete student
@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
