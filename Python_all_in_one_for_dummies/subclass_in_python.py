import datetime as dt
from re import M
# Class is used for all kinds of people

# Base class is used for all kinds of Members
class Member:
    """ The Member class attributes and methods are for everyone """
    # By default, a new account expires in one year (365 days)
    expiry_days = 365

    # Initialize a member object.
    def __init__(self, firstname, lastname):
        # Attributes (instane variables) for evrybody.
        self.firstname = firstname
        self.lastname = lastname
        # Calculate expiry date from today's date.
        self.expiry_date = dt.date.today() + dt.timedelta(days = self.expiry_days)
        # Default secret code is nothing
        self.secret_code = ''

    # Method in the base class
    def showexpiry(self):
        return f"{self.firstname} {self.lastname} expires on {self.expiry_date}"

# Subclass for Admins.
class Admin(Member):
    # Admin accounts don't expire for 100 years
    expiry_days = 365.222 * 100
    #Sublcass parameters
    def __init__(self, firstname, lastname, secret_code):
        # Pass Member parameters on up to Member class.
        super().__init__(firstname, lastname)
        # Assign the remaining parameter to this object
        self.secret_code = secret_code
    

#Subclass for users.
class User(Member):
    pass

Ann = Admin('Annie','Angst', 'PRESTO')
print(Ann.showexpiry())
# print(Ann.firstname, Ann.lastname, Ann.expiry_date, Ann.secret_code)

print()
Uli = User('Uli','Ungula')
print(Ann.showexpiry())
# print(Uli.firstname, Uli.lastname, Uli.expiry_date)

help(Admin)