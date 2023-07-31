from flask import Flask, redirect, render_template, flash, url_for, request
import sqlite3 as sql

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    return render_template('index.html', datas=data)

@app.route('/add_products', methods=['POST', 'GET'])
def add_products():
    if request.method == 'POST':
        Product_Name = request.form['Product_Name']
        Type = request.form['Type']
        Brand = request.form['Brand']
        Price = request.form['Price']
        MadeIn = request.form['MadeIn']

        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("INSERT INTO products (Product_Name, Type, Brand, Price, MadeIn) values (?,?,?,?,?)", (Product_Name, Type, Brand, Price, MadeIn))
        con.commit()
        flash("Product Added", "success")
        return redirect(url_for('index'))
    return render_template('add_product.html')

@app.route('/edit_product/<strig:id>', methods=['POST', 'GET'])
def edit_product(id):
    if request.method == 'POST':
        Product_Name = request.form['Product_Name']
        Type = request.form['Type']
        Brand = request.form['Brand']
        Price = request.form['Price']
        MadeIn = request.form['MadeIn']

        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("UPDATE products SET Product_Name=?, Type=?, Brand=?, Price=?, MadeIn=? WHERE ID=?", (Product_Name, Type, Brand, Price, MadeIn, id))
        con.commit()
        flash("Product Updated", "success")
        return redirect(url_for('index'))
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM products WHERE ID=?', (id,))
    data = cur.fetchone()
    return render_template('edit_product.html', datas=data)

@app.route('/delete_product/<string:id>', methods=['GET'])
def delete_product(id):
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute("DELETE * FROM products WHERE ID=?", (id,))
    con.commit()
    flash("Product Deleted", "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = 'admin123'
    app.run(debug=True)
