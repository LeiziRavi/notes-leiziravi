import datetime as dt
# Define a new class name Member.
class Member:
    # Defualt number of free days.
    free_days = 365


    """Create a new member. """
    def __init__(self, username, fullname):
        self.date_joined = dt.date.today()  
        # set an expiration date
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)

# the class ends at the first un-indented line.

Member.free_days = 100
# Create an instance of the Member class named new_guy.
wilbur = Member('wblomgren', 'Wilbur Blomegren')

# But if printed, on its own will print the changed information.
print(Member.free_days) # prints 100 not 365
print(wilbur.date_joined)
print(wilbur.free_expires) # Uses 365 as intended, cannot be changed from outside.

Member.free_days = 10
samar = Member('samaritan','samar joe')
print(samar.date_joined)
print(samar.free_expires)
# Class_methods will always use the class_variable value, not the modified value outside of the class.