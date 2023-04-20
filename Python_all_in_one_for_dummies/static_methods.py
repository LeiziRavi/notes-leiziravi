import datetime as dt

# Define a class named Member for making member objects
class Member:
    # This is a class variable that's the same for all instances.
    free_days = 0

    """Create a member object from username and fullname"""
    def __init__(self) -> None:
        #Define properties and assign default values
        self.date_joined = dt.date.today()
        self.free_expires = dt.date.today() + dt.timedelta(Member.free_days)


    #Class methods follow @classmethods and use cls rather then self
    @classmethod
    def setfreedays(cls, days):
        cls.free_days = days

    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%I:%M %p}"

# Class definition ends at last indented line
# Try out the new static method (no object required)
print(Member.currenttime()) 