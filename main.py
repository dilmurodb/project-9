from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

intro_question = input("What would you like to do with Contacts? Create? Read? Find? Delete? Update? ")


def read_contact():
    contacts = Contact.select()
    for contact in contacts:
        print(contact)
        print(contact.firstname + " " + contact.lastname + " " + contact.phone + " " + contact.email + " " + contact.address)


def create_contact():
    contact_firstname = input("Enter First Name: ")
    contact_lastname = input("Enter Last Name: ")
    contact_phone = input("Enter Phone Number: ")
    contact_email = input("Enter Email: ")
    contact_address = input("Enter Address: ")
    newcontact = Contact(firstname = contact_firstname, lastname = contact_lastname, phone = contact_phone, email = contact_email, address = contact_address)
    newcontact.save()
    print(newcontact.firstname + " " + newcontact.lastname + " " + newcontact.phone + " " + newcontact.email + " " + newcontact.address)

def update_contact():
    update_find_by_firstname = input("Enter the First Name of the contact you want to update: ")
    updated_info = Contact.get(Contact.firstname == update_find_by_firstname)
    new_phone = input("Enter the new number: ")
    updated_info.phone = new_phone
    new_email = input("Enter new Email: ")
    updated_info.email = new_email
    new_address = input("Enter new Address: ")
    updated_info.address = new_address
    updated_info.save() 


def find_contact():
    find_contact_by_firstname = input("Enter First Name of the contact you want to find: ")
    find_by_firstname = Contact.get(Contact.firstname == find_contact_by_firstname)
    print(find_by_firstname.firstname + " " + find_by_firstname.lastname + " " + find_by_firstname.phone + " " + find_by_firstname.email + " " + find_by_firstname.address)

def delete_contact():
    contact_name_delete = input("Enter First Name of the contact you want to delete: ")
    contact_firstname = Contact.get(Contact.firstname == contact_name_delete)
    contact_firstname.delete_instance()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    firstname = CharField()
    lastname = CharField()
    phone = CharField()
    email = CharField()
    address = CharField()

db.connect()
db.create_tables([Contact])

if intro_question == "Create":
    create_contact()


elif intro_question == "Read":
    read_contact()


elif intro_question == "Delete":
    delete_contact()

elif intro_question == "Find":
    find_contact()

elif intro_question == "Update":
    update_contact()