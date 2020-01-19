from peewee import *
# from datetime import date

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

intro_question = input("What would you like to do with Contacts? Create? Read? Delete? ")
# contact_info = input("Please enter your contact info:")


def read_contact():
    contacts = Contact.select()
    for contact in contacts:
        print(contact)
        print(contact.name + " " + contact.phone + " " + contact.email + " " + contact.address)
        # print(contact.name)

# def update_contact(update_contact):
#     contacts = Contact.get(Contact.name == update_contact)
#     Contact.phone =

def create_contact():
    contact_name = input("Enter First Name: ")
    contact_phone = input("Enter Phone Number: ")
    contact_email = input("Enter Email: ")
    contact_address = input("Enter Address: ")
    newcontact = Contact(name = contact_name, phone = contact_phone, email = contact_email, address = contact_address)
    newcontact.save()
    print(newcontact.name + " " + newcontact.phone + " " + newcontact.email + " " + newcontact.address)

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    name = CharField()
    phone = CharField()
    email = CharField()
    address = CharField()
# read_contact()
db.connect()
db.create_tables([Contact])

if intro_question == "Create":
    # contact_input = input("Enter contact First Name: ")
    create_contact()


elif intro_question == "Read":
    update_contact = input("Enter First Name: ")
    read_contact()

    # update_contact = input("Enter Phone Number: ")
    # update_contact = input("Enter Email: ")


elif intro_question == "Delete":
    delete_contact = input("Enter the Full Name of the contact you want to delete: ")



#remove this when you want your database to start saving forever
# db.drop_tables([Contact])

db.create_tables([Contact])

dilmurod = Contact(name='Dilmurod Bukharov', phone='4121234567', 
email='d.bukharov@gmail.com', address='Washington DC')
someperson = Contact(name='Some Person', phone='9876543251', 
email='d.bukharov@ganymail.com', address='NYC')
dilmurod.save()
someperson.save()

# read_contact()