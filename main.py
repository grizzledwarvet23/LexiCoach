from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create-vocablist')
def create_vocablist():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def process_submittedlist():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Data received successfully'})


if __name__ == '__main__':
    app.run(debug=True)




