"""
    test a SQLite database connection locally
    assumes database file is in same location
    as this .py file
"""
import os
import random
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
    return render_template('home.html',names=all_lists)
    
@app.route('/donate')
def donation():
    return render_template('donation.html')


@app.route('/practice')
def practice():
    search = request.args.get('listname', '')
    k = db.session.execute(db.select(VocabList).filter_by(name = search)).scalars().first()
    if(k == None):
        return("<p>Sorry: we couldn't find a vocab list with that name.</p><a href = '/'>Home</a>")
    words = k.vocab.split(",")
    random.shuffle(words)
    lan = k.language
    toret = ""
    
    s = gen_sent(words,lan)
    
    return render_template('practice.html',sentences=s)
    

@app.route('/create-vocablist')
def create_vocablist():
    return render_template('create.html')

@app.route('/edit')
def edit():
    search = request.args.get('listname', '')
    k = db.session.execute(db.select(VocabList).filter_by(name = search)).scalars().first()
    if(k == None):
        return("<p>Sorry: we couldn't find a vocab list with that name.</p><a href = '/'>Home</a>")
    words = k.vocab.split(",")
    ff = [""]*5
    overflows = []
    for i in range(len(words)):
        if i < 5:
            ff[i] = words[i]
        else:
            overflows += [(i+1,words[i])]


    return render_template('edit.html',t1=ff[0],t2=ff[1],t3=ff[2],t4=ff[3],t5=ff[4],overflow=overflows,title=k.name,lang=k.language)

@app.route('/addlist')
def add():


    voc = request.args.get('vocab', '')
    lan = request.args.get('language', '')
    name = request.args.get('name', '')
    
    k = db.session.execute(db.select(VocabList).filter_by(name = name)).scalars().first()
    if(not k == None):
        return("<p>Sorry: you already made a vocab list with that name.</p><a href = '/'>Home</a>")

    l = VocabList()
    l.vocab = voc
    l.language = lan
    l.name = name
    db.session.add(l)
    db.session.commit()

    all_lists = db.session.execute(db.select(VocabList.name)).scalars()
    return render_template('home.html',names=all_lists)
@app.route('/editlist')
def editlist():
    voc = request.args.get('vocab', '')
    lan = request.args.get('language', '')
    name = request.args.get('name', '')
    
    k = db.session.execute(db.select(VocabList).filter_by(name = name)).scalars().first()
    if(k == None):
        return("<p>Sorry: you can't edit a vocab list that doesn't exist.</p><a href = '/'>Home</a>")


    k.vocab = voc
    k.language = lan
    k.name = name
    db.session.commit()

    all_lists = db.session.execute(db.select(VocabList.name)).scalars()
    return render_template('home.html',names=all_lists)



if __name__ == '__main__':
    app.run(host="localhost",port=6060, debug=False)