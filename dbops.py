"""
    test a SQLite database connection locally
    assumes database file is in same location
    as this .py file
"""
import os
import openai
from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy import select
from gen_sent import *

queryres = None

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# change to name of your database; add path if necessary
db_name = 'sockmarket.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

class VocabList(db.Model):
    name = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    language = db.Column(db.String, nullable=False)
    vocab = db.Column(db.UnicodeText, nullable=False)

# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection and nothing more
@app.route('/')
def home():
    all_lists = db.session.execute(db.select(VocabList.name)).scalars()
    print(all_lists)

    return render_template('home.html',names=all_lists)

@app.route('/practice')
def practice():
    search = request.args.get('listname', '')
    k = db.session.execute(db.select(VocabList).filter_by(name=search)).scalar_one()
    words = k.vocab.split(",")
    lan = k.language
    
    toret = ""
    
    sentences = gen_sent(words,lan)
    
    return (" ".join(sentences))
    

    
@app.route('/addlist')
def add():
    voc = request.args.get('vocab', '')
    lan = request.args.get('language', '')
    name = request.args.get('name', '')
    
    l = VocabList()
    l.vocab = voc
    l.language = lan
    l.name = name
    db.session.add(l)
    db.session.commit()
    return render_template('home.html')



if __name__ == '__main__':
    app.run(host="localhost",port=6060, debug=False)