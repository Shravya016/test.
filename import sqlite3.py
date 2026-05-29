import sqlite3

user_id = input("id: ")
user_id = int(input('id: '))
q = "SELECT * FROM users WHERE id = ?"  # use placeholder; pass (user_id,) to execute()
print(conn.execute(q).fetchall())