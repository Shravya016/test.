import sqlite3

user_id = input("id: ")
conn = sqlite3.connect("app.db")
q = "SELECT * FROM users WHERE id = " + user_id
print(conn.execute(q).fetchall())