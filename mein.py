import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                 (f"User{i}", f"example{i}@gmail.com", f'{i}0', 100000))
#
#
# for ij in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, ij))
#
# for ih in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (ih,))


cursor.execute("DELETE FROM Users WHERE id = 6")

# cursor.execute("SELECT COUNT(*) FROM Users")
# total1 = cursor.fetchone()[0]
# print(total1)
#
# cursor.execute("SELECT SUM(balance) FROM Users")
# total2 = cursor.fetchone()[0]
# print(total2)

cursor.execute("SELECT SUM(balance) FROM Users")
total3 = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM Users")
total4 = cursor.fetchone()[0]
print(total3, total3/total4)


connection.commit()


# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(user)

connection.close()
