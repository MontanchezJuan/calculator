from flask import Flask, request, jsonify

app = Flask(__name__)


# Endpoint para sumar
@app.route('/calculator/addition', methods=['POST'])
def addition():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])

    resp = num1 + num2

    return jsonify({"respuesta": f"El resultado de la suma es: {resp}"})

# Endpoint para multiplicación 
@app.route('/calculator/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])

    resp = num1 * num2

    return jsonify({"respuesta": f"El resultado de la multipilcación es: {resp}"})

if __name__ == '__main__':
    app.run(debug=True)
