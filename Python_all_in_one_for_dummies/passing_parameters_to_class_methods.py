import datetime as dt

# define a new class name member
class Member:
    """ Create a new member. """
    def __init__(self, username, fullname):
        # Define attributes and give them values.
        self.username = username
        self.fullname = fullname
        # Default date_joined to today's date/
        self.date_joined = dt.date.today();
        # Set is active to True initially
        self.is_active = True

    # A method to return a formatted string with showing date joined.
    def show_datejoined(self):
        return f"{self.fulltime} joined on {self.date_joined:%m%d%y}"

    # Method to activate (True) or deactive (False) account.
    def activate(self, yesno):
        """True for active, False to make inactive """
        self.is_active = yesno

# The class ends at the first un_indented line.

# Create an instance of the Member class named new_guy
new_guy = Member('Rambo','Rocco Moe')

# Is new_guy active?
print(new_guy.is_active)

# Try out the activate method
new_guy.activate(False)

# Is new_guy still active?
print(new_guy.is_active)