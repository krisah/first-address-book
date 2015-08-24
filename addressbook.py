import sys

print "Welcome to my address book"

#class contact:
def __init__(self,firstName,lastName,phone,email,address):
      self.firstName = firstName
      self.lastName = lastName
      self.phone = phone
      self.email = email
      self.address = address

def collectContact():
      firstName = raw_input("What is the contacts first name?")
      lastName = raw_input("What is the contacts last name?")
      phone = raw_input("What is the contacts phone number?")
      email = raw_input("What is the contacts email?")
      address = raw_input("What is the contacts address?")

      contactInfo = (firstName + " " + lastName + "," + phone + "," + email + "," + address) 

      append_to_database(contactInfo)

#class addressBook:
def append_to_database(contactInfo):
      addressbook1 = open("addressbook.txt" , "a")
      addressbook1.write(contactInfo)
      addressbook1.write("\n")
      addressbook1.close()
      print "The data has been add to the address book."

def search_database():
      searchInput = raw_input("Please enter what you are searching for?")
      addressbook1 = open("addressbook.txt","r")
      for i in addressbook1:
            if searchInput in i:
                print("\n")
                print i
                break
      else:
            print "Search results returned zero results"


#class startMenu:
def menu():
      startProgram = raw_input("Are you creating an entry or searching for an entry? Enter creating or searching")
      if startProgram == "creating":
           collectContact()
      elif startProgram == "searching":
           search_database()
      else:
            print str(startProgram) + " is not a valid option. You need to try again"
            menu()
menu()
