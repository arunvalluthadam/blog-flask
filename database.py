import sqlite3

db = sqlite3.connect('dataPost.db')
cur = db.cursor()
cur.execute("CREATE TABLE if not EXISTS blogdata (id INTEGER PRIMARY KEY, name TEXT, place TEXT)")
db.commit()
db.close()