dog_years = float(input("Enter dog years: "))
human_years = 0

if dog_years < 0:
    print("Enter valid age, age cannot be negative.")
elif dog_years <= 2:
    human_years = dog_years * 10.5
else:
    human_years = 21 + ((dog_years-2) * 4)

print(f"{dog_years} human years is dog years is: {human_years}")
