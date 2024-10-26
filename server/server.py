from flask import Flask, request, jsonify

import mysql.connector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from engine.engine import AST

db_config = {
    "user": "root",
    "password": "Example@2022#",
    "host": "localhost",
    "database": "rule_engine",
}

app = Flask(__name__)

ast=AST()

@app.route('/process', methods=['GET'])
def process_string():
    # Get the string from the query parameter
    rule_name = request.args.get('rule_name')
    input_string = request.args.get('input_string')

    if input_string is None:
        return jsonify({"error": "No input string provided"}), 400

    # add code to validate
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(f"""insert into rules values ("{rule_name}", "{input_string}")""")
    connection.commit()
    cursor.close()
    connection.close()
    # Process the string (e.g., reverse it as an example)
    # ast.set_root(ast.create_rule(input_string))/
    return jsonify({"response": f"rule stored with rule name {rule_name}"})


@app.route('/evaluate/<name>', methods=['POST'])
def evaluate_json(name):
    # Get the JSON object from the request body
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(f""" SELECT rule FROM rules where name="{name}" """)
    result=cursor.fetchall()
    cursor.close()
    connection.close()

    rule=result[0][0]
    ast.set_root(ast.create_rule(rule))
    return jsonify({"result": ast.evaluate_rule(data)})


if __name__ == '__main__':
    app.run(port=8000, debug=True)  # Set the desired port here

