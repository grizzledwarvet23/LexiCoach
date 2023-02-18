from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create-vocablist')
def create_vocablist():
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)




