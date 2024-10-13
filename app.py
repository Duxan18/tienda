from flask import Flask, request, jsonify, render_template
from datetime import datetime, time
import atexit

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
    return render_template('index.html')  # Asegúrate de que 'index.html' esté en una carpeta llamada 'templates'

@app.route('/subir_valor', methods=['POST'])
def subir_valor():
    valor = request.json.get('valor', 0)
    valores.append(valor)
    return jsonify({"message": "Valor agregado exitosamente."})

@app.route('/obtener_suma', methods=['GET'])
def obtener_suma():
    total = sum(valores)
    return jsonify({"suma_total": total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
