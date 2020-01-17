from peewee import *
from datetime import date

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

contact_info = input("Please enter your contact info:")

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    name = CharField()
    birthday = DateField()
    phone = CharField()
    email = CharField()
    address = CharField()

db.connect()

#remove this when you want your databvase to start saving forever
db.drop_tables([Contact])

db.create_tables([Contact])

dilmurod = Contact(name='Dilmurod Bukharov', birthday=date(1989, 11, 17), phone='4121234567', 
email='d.bukharov@gmail.com', address='Washington DC')
dilmurod.save()