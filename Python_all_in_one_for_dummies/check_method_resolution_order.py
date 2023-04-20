import datetime as dt
from re import M
# Class is used for all kinds of people

# Base class is used for all kinds of Members
class Member:
    """ The Member class attributes and methods are for everyone """

    # Initialize a member object.
    def __init__(self, firstname, lastname):
        # Attributes (instane variables) for evrybody.
        self.firstname = firstname
        self.lastname = lastname
       
    # Method in the base/main class
    def get_status(self):
        return f"{self.firstname} is a Member."

# Subclass for Admins.
class Admin(Member):
   # Method in the admin class
    def get_status(self):
        return f"{self.firstname} is an Admin."
    

#Subclass for users.
class User(Member):
   # Method in the User class
    def get_status(self):
        return f"{self.firstname} is a regular user."

#Create an admin
Ann = Admin('Annie','Angst')
print(Ann.get_status())

print()
# Create a User
Uli = User('Uli','Ungula')
print(Ann.get_status())

print()
# Create a Member
Manny = User('Mindy','Membo')
print(Manny.get_status())

# help(Admin)