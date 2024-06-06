# models.py

import sqlite3

class Alumno:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alumnos')
    data = cursor.fetchall()
    conn.close()
    return data
