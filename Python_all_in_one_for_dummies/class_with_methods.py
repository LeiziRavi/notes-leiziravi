import datetime as dt

# Define a new class name Member.
class Member:
    """ Create a new member. """
    def __init__(self, uname, fname):
        # Define attributes and give them values.
        self.username = uname
        self.fullname = fname

        # Default date_joined to today's date.
        self.date_joined = dt.date.today()
        # Set is_active to true initially.
        self.is_active = True
    
    # Methods for each instance created (instance methods)

    # A method to return a formatted string with showing date joined
    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined:%m/%d/%y}"

# The class ends at the first un-idented line.

# Create an instance of the Member class named new_guy
new_guy = Member('Rambo','Rocco Moe')

# See what's in the instance, as well as its individual properties.
print(new_guy.show_datejoined())