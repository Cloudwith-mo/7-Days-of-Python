from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify(message="Ahoy, World!")

if __name__ == '__main__':
    app.run(debug=True)