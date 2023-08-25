from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para sumar
# Recibe dos numeros de los cuales suma el primer número por el segundo
@app.route('/calculator/addition', methods=['POST'])
def addition():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])

    resp = num1 + num2

    return jsonify({"respuesta": f"El resultado de la suma es: {resp}"})

# Endpoint para restar
# Recibe dos numeros de los cuales resta el segundo número al primer número
@app.route('/calculator/subtraction', methods=['POST'])
def subtraction():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])

    resp = num1 - num2

    return jsonify({"respuesta": f"El resultado de la resta es: {resp}"})

# Endpoint para multiplicación
# Recibe dos numeros de los cuales multiplica el primer número por el segundo
@app.route('/calculator/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])

    resp = num1 * num2

    return jsonify({"respuesta": f"El resultado de la multipilcación es: {resp}"})

# Endpoint para dividir 
# Recibe dos numeros de los cuales divide el segundo número al primer número
# Además se valida la división entre 0, si es así se retorna una respuesta diferente
@app.route('/calculator/division', methods=['POST'])
def division():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])

    if num2 == 0:
        return jsonify({"respuesta": f"No es posible hacer una división por 0"})

    resp = num1 / num2

    return jsonify({"respuesta": f"El resultado de la división es: {resp}"})

if __name__ == '__main__':
    app.run(debug=True)
