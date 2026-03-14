import sqlite3
conn = sqlite3.connect("database.db") 
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
            )
""")
conn.commit()
print('Виберіть дію:')
print('1. Додати користувача')
print('2.Видалити користувача')
print('3. Показати всіх користувачів')
choice=input('Введіть номер дії: ')
if choice=='1':
    name=input("Введіть ім'я користувача: ")
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    print(f"Користувач '{name}' доданий до бази даних.")
elif choice=='2':
    user_id=input("Введіть ID користувача для видалення: ")
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print(f"Користувач з ID {user_id} видалений з бази даних.")
elif choice=='3':
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("Користувачі в базі даних:")
    for user in users:
        print(f"ID: {user[0]}, Ім'я: {user[1]}")
else:
    print("Невірний вибір. Будь ласка, виберіть 1, 2 або 3.")
conn.close()
# name=input("Enter your name: ")
# cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
# conn.commit()
# cursor.execute("SELECT * FROM users")
# users = cursor.fetchall()
# print("Users in the database:")
# for user in users:
#     print(f"ID: {user[0]}, Name: {user[1]}")
# conn.close()