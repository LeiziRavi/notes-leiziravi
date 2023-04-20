ROI = 0.04
p = float(input("Enter the principal amount: "))

p1 = p + (p*ROI)
p2 = p1 + (p1*ROI)
p3 = p2 + (p2*ROI)

print("Amount in savings account: ")
print("\tAfter one year: %.2f Rs. \n\tAfter two year: %.2f Rs. \n\tAfter three year: %.2f Rs. \n" % (p1, p2, p3))
