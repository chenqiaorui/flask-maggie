import peewee

db = peewee.SqliteDatabase('books.db')


class Book(peewee.Model):
    title = peewee.CharField()
    author = peewee.CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Book])

book = Book(title='Python入门', author='张三')
book.save()
