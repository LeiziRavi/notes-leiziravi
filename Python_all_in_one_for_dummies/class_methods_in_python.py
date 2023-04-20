import datetime as dt
# define a new class name Member.
class Member:
    # Default number of free days.
   
    free_days = 365

    """Create a new member. """
    def __init__(self, username, fullname):
        self.date_joined = dt.date.today()
        # Set an expiration date
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)

    # Class methods follow @classmethod decorator and refer to cls rather then to self
    @classmethod
    def setfreedays(cls, days):
        cls.free_days = days

Member.setfreedays(30)

print(Member.free_days)