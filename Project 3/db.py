import sqlite3 as sql

con = sql.connect('database.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS products')

sql = """CREATE TABLE "products" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Product_Name" TEXT,
    "Type" TEXT,
    "Brand" TEXT,
