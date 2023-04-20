LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

more_Than_1L = int(
    input("Enter the values for number of containers capacity > 1L : "))
less_Than_1L = int(
    input("Enter the values for number of containers capacity < 1L : 5"))

refund = (LESS_DEPOSIT * less_Than_1L) + \
    (MORE_DEPOSIT * more_Than_1L)
print("Refund for returning containers: $ %0.2f" % refund)
