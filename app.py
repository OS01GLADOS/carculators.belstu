from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from CalculatorsScripts.ExEvclid import GetBigger
from CalculatorsScripts.DiophantineEquations import DiophaniteRight
from CalculatorsScripts.PrimeFactorization import PrimeFactor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///mysite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


database = SQLAlchemy(app)

"""
class Messages(database.Model):
    __tablename__ = 'Messages'
    id = database.Column(database.Integer, primary_key=True)
    textMessage = database.Column(database.String(500))
    author = database.Column(database.String(128), database.ForeignKey('Users.username'))
    creationDate =database.Column(database.DateTime(),default=datetime.now)
    posts = database.relationship('Users',backref='Messages')
    def __repr__(self):
        return '<Messages  %r>' % self.id


class Users(database.Model):
    __tablename__ = 'Users'
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(128), unique=True )
    password_hash = database.Column(database.Integer)
    registrationDate = database.Column(database.DateTime(),default=datetime.now)
    def __repr__(self):
        return '<Users  %r>' % self.id

"""
@app.route('/')
def FirstPage():
    return render_template('Index.html')

@app.route('/calculators/ExEvclid', methods=["POST","GET"])
def ExEvclid():
    if request.method =="POST":
        A = int(request.form['numberA'])
        B = int(request.form['numberB'])
        res = GetBigger(A,B)
        return render_template('Calculators/ExEvclid.html',ResultExEvclid=res)
    else:
        return render_template('Calculators/ExEvclid.html')

@app.route('/calculators/DiophantineEquations', methods=["POST","GET"])
def DioEquations():
    if request.method =="POST":
        a = int(request.form['numberA'])
        b = int(request.form['numberB'])
        c = int(request.form['numberC'])
        tBegin = int(request.form['numberBegin'])
        tEnd = int(request.form['numberEnd'])
        DiophantineResult = DiophaniteRight(a,b,c, tBegin,tEnd)
        return render_template('Calculators/DiophantineEquations.html', ResultExEvclid=DiophantineResult.resEvclid, DiophantineRes=DiophantineResult, tBegin=tBegin, tEnd=tEnd)
    else:
        return render_template('Calculators/DiophantineEquations.html')

@app.route('/calculators/PrimeFactorization', methods=["POST", "GET"])
def Factorization():
    if request.method=="POST":
        number = int(request.form['number'])
        res = PrimeFactor(number)
        return  render_template('Calculators/PrimeFactor.html',Answer = res)
    else:
        return render_template('Calculators/PrimeFactor.html')


if __name__ == '__main__':
    app.run(debug=True)