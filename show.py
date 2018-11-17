from database import Database

db = Database()
db.load('accounts.db')
print(db.data)
