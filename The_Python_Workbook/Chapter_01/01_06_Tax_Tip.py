meal_cost = float(input("Enter the cost of the meal ordered: "))
GST = 0.025
TIP_Percent = 0.18
tax = meal_cost * GST
tip = meal_cost * TIP_Percent
total_bill = meal_cost + tax + tip
# print("tax amount: $ %.2f" % tax, "tip amount: $ %.2f" %
#       tip, "grand total: $ %.2f" % total_bill)
print("tax amount: $ %.2f, tip amount: $ %.2f, grand total: $ %.2f" %
      (tax, tip, total_bill))
