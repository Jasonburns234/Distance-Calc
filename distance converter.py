name = input("Enter your first name: ")
kilometer = float(input("Enter a distance in kilometers: "))
miles = kilometer * 0.62137
print(f"Hi {name.title()}! {kilometer} kilometer is equivalent to  {round(miles, 1)} miles.")
