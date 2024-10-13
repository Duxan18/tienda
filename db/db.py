import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='tu_usuario',
        password='tu_contraseña',
        database='gastos_db'
    )
    return connection
