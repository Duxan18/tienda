import sqlite3
import os
from app import Flask

app = Flask(__name__)

def init_db():
    # Conectar a la base de datos (o crearla si no existe)
    conn = sqlite3.connect('gastos.db')
    
    # Leer el archivo SQL
    sql_script_path = os.path.join(os.path.dirname(__file__), 'create_table.sql')
    
    with open(sql_script_path, 'r') as file:
        sql_script = file.read()

    # Ejecutar el script
    try:
        conn.executescript(sql_script)
        print("Tabla creada con éxito.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        conn.close()

# Inicializar la base de datos al iniciar la aplicación
if __name__ == '__main__':
    init_db()  # Llama a la función para crear la tabla
    app.run(debug=True)  # Asumiendo que 'app' es tu instancia de Flask
