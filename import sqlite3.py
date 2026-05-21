import sqlite3

user_id = input("id: ")
conn = sqlite3.connect("app.db")
q = "SELECT * FROM users WHERE id = ?"  # use placeholder; pass (user_id,) to execute()
print(conn.execute(q).fetchall())