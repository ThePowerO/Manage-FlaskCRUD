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
    if request.method == "POST":
        이름 = request.form['이름']
        나이 = request.form['나이']
        거리 = request.form['거리']
        도시 = request.form['도시']
        전화_번호 = request.form['전화_번호']
        이메일 = request.form['이메일']

        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute('INSERT INTO users (이름, 나이, 거리, 도시, 전화_번호, 이메일) values (?,?,?,?,?,?)', (이름, 나이, 거리, 도시, 전화_번호, 이메일))
        con.commit()
        flash("데이터 등록했어요 (Data Registered)", "success")
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route('/edit_user/<string:id>', methods=['POST', 'GET'])
def edit_user(id):
    if request.method == "POST":
        이름 = request.form['이름']
        나이 = request.form['나이']
        거리 = request.form['거리']
        도시 = request.form['도시']
        전화_번호 = request.form['전화_번호']
        이메일 = request.form['이메일']

        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute('UPDATE users SET 이름=?, 나이=?, 거리=?, 도시=?, 전화_번호=?, 이메일=? WHERE ID=?', (이름, 나이, 거리, 도시, 전화_번호, 이메일, id))
        con.commit()
        flash("데이터 등록했어요 (Data Updated)", "success")
        return redirect(url_for("index"))
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE ID=?', (id,))
    data = cur.fetchone()
    return render_template('edit_user.html', datas=data)

@app.route('/delete_user/<string:id>', methods=['GET'])
def delete_user(id):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE ID=?", (id,))
    con.commit()
    flash("데이터 삭젰어요 (Data Deleted)", "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = "admin123"
    app.run(debug=True)
