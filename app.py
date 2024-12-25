from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

value_counts = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_value():
    value = request.json.get('value')  
    if not value:
        return jsonify({"error": "No value provided"}), 400
    
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1
    
    return jsonify({"count": value_counts[value]})  

@app.route('/values', methods=['GET'])
def get_values():
    return jsonify(value_counts)  


if __name__ == '__main__':
    app.run(debug=True)
