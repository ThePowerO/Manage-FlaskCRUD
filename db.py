import sqlite3 as sql

con = sql.connect("database.db")
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = """CREATE TABLE "users" (

    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "이름" TEXT,
    "나이" TEXT,
    "거리" TEXT,
    "도시" TEXT,
    "전화_번호" TEXT,
    "이메일" TEXT

)"""

cur.execute(sql)
con.commit()
con.close()
