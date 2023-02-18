from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create-vocablist')
def create_vocablist():
    print('Button clicked')
    return 'Button clicked'

if __name__ == '__main__':
    app.run(debug=True)




