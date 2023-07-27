from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

app.route('/')
app.route('/index')
def index():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM GiveAways")
    data = cur.fetchall()
    return render_template('index.html', datas=data)

app.route('/add_giveaway', methods=['POST', 'GET'])
def Add_GiveAway():
    if request.method == 'POST':
        GiveAway_Name = request.form['GiveAway Name']
        Type = request.form['Type']
        Reward = request.form['Reward']
        Entries = request.form['Entries']
        Max_Winners = request.form['Max Winners']
        Initial_Date = request.form['Initial Date']
        Duration = request.form['Duration']

        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("INSERT INTO GiveAways (GiveAway Name, Type, Reward, Entries, Max Winners, Initial Date, Duration) values (?,?,?,?,?,?,?,?)", (GiveAway_Name, Type, Reward, Entries, Max_Winners, Initial_Date, Duration))
        con.commit()
        flash("Giveaway Created", "success")
        return redirect(url_for('index.html'))
    return render_template('add_giveaway.html')

app.route('/edit_giveaway/<string:id>', method=['POST', 'GET'])
def edit_giveaway(id):
    if request.method == 'POST':
        GiveAway_Name = request.form['GiveAway Name']
        Type = request.form['Type']
        Reward = request.form['Reward']
        Entries = request.form['Entries']
        Max_Winners = request.form['Max Winners']
        Initial_Date = request.form['Initial Date']
        Duration = request.form['Duration']

        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("UPDATE GiveAways SET GiveAway Name=?, Type=?, Reward=?, Entries=?, Max Winners=?, Initial Date=?, Duration=? WHERE ID=?", (GiveAway_Name, Type, Reward, Entries, Max_Winners, Initial_Date, Duration, id))
        con.commit()
        flash("Giveaway Edited", "success")
        return redirect(url_for('index.html'))
    return render_template('edit_giveaway.html')

@app.route('/delete_giveaway/<string:id>', methods=['GET'])
def delete_giveaway(id):
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute("DELETE FROM GiveAways WHERE id=?", (id))
    con.commit()
    flash("Giveaway Deleted", "success")
    return redirect(url_for('index.html'))

if __name__ == "__main__":
    app.secret_key = "admin123"
    app.run(debug=True)
