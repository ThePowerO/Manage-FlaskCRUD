from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return render_template('index.html', datas=data)

@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.mothod == "POST":
        이름 = request.form['이름']
        나이 = request.form['나이']
        거리 = request.form['거리']
        도시 = request.form['도시']
        전화_번호 = request.form['전화_번호']
        이메일 = request.form['이메일']

        con = sql.connect('database.db')
