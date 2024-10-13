from flask import Flask, request, jsonify, render_template
from datetime import datetime, time
import atexit
from db.db import create_connection

app = Flask(__name__)

valores = []

def reset_values():
    global valores
    current_time = datetime.now().time()
    if current_time >= time(22, 0) and current_time < time(22, 5):
        valores = []

atexit.register(reset_values)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subir_valor', methods=['POST'])
def subir_valor():
    valor = request.json.get('valor', 0)
    detalle = request.json.get('detalle', 'No informa')
    fecha = datetime.now()

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO datos (fecha, valor, detalle) VALUES (%s, %s, %s)", (fecha, valor, detalle))
    connection.commit()
    cursor.close()
    connection.close()

    valores.append(valor)
    return jsonify({"message": "Valor y detalle agregados exitosamente."})


@app.route('/obtener_suma', methods=['GET'])
def obtener_suma():
    total = sum(valores)
    return jsonify({"suma_total": total})

def init_db():
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS datos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fecha TIMESTAMP NOT NULL,
        valor DECIMAL(10, 2) NOT NULL,
        detalle VARCHAR(255) DEFAULT 'No informa'
    )
    ''')
    
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)