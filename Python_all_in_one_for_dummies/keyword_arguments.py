def hello(fname, lname, datestring):  # Practice function
    """A doctstring describing the function"""
    msg = "Hello " + fname + " " +lname
    msg += " you mentioned " + datestring
    print(msg)


# Pass in liternal kwargs (identify each by parameter name)
hello(datestring='12/31/2019', lname='Simpson', fname='Alan')

# Pass in in kwrgs from variables (identify each by parameter name)
apt_date = '12/30/2019'
last_name = 'Janda'
first_name = 'Kylie'
hello(datestring=apt_date, lname=last_name, fname=first_name)
