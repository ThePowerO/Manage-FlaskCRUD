import sqlite3 as sql

con = sql.connect('database.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS giveaways")

sql = """CREATE TABLE 'GiveAways' (
       "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
       "GiveAway_Name" TEXT,
       "Type" TEXT,
       "Reward" TEXT,
       "Entries" TEXT,
       "Max_Winners" TEXT,
       "Initial_Date" TEXT,
       "Duration" TEXT

)"""

cur.execute(sql)
con.commit()
con.close()
