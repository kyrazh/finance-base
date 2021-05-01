from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from parsusd import curs


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:qwerty@localhost:5432/Data"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summa = db.Column(db.Float)
    summausd = db.Column(db.Float)
    optype = db.Column(db.String)
    currentdate = db.Column(db.DateTime)
    comment = db.Column(db.String(100))

    def __init__(self, summa, summausd, optype, comment, currentdate):
        self.summa = summa
        self.summausd = summausd
        self.optype = optype
        self.comment = comment
        self.currentdate = currentdate


@app.route('/')
def index():
    all_data = Data.query.all()

    return render_template("index.html", records=all_data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        summa = request.form['summa']
        optype = request.form['optype']
        comment = request.form['comment']
        currentdate = datetime.utcnow()
        summausd = round(((float(summa)) / curs), 2)

        my_data = Data(summa, summausd, optype, comment, currentdate)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.summa = request.form['summa']
        my_data.optype = request.form['optype']
        my_data.comment = request.form['comment']

        db.session.commit()

        return redirect(url_for('index'))


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
