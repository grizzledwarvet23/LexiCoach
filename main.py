from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create-vocablist')
def create_vocablist():
    return render_template('create.html')

@app.route('/create', methods=['GET', 'POST'])
def process_submittedlist():
    if request.method == 'POST':
        vocablist_title = request.form['vocablist-title']
        language = request.form['language']
        terms = [request.form[f'term{i}'] for i in range(1, 6)]

        new_vocablist = {
            'title': vocablist_title,
            'language': language,
            'terms': terms
        }

        print(terms)
        return render_template('home.html', vocablist=new_vocablist)


    data = request.get_json()
    print(data)
    return jsonify({'message': 'Data received successfully'})


if __name__ == '__main__':
    app.run(debug=True)




