print("Welcome to Izifin Technology, a Fintech company in Nigeria with about 2500 staff strength with various years of work experience.")

age = int(input("Enter age: "))
years_of_experience = int(input("How many years of experience do you have: "))

if age >= 55 and years_of_experience > 25:
     Annual_tax_revenue = 5600000
elif years_of_experience > 20 and age >= 45:
     Annual_tax_revenue = 4480000

elif age >= 35 and years_of_experience > 10:
     Annual_tax_revenue = 1500000
else: 
     Annual_tax_revenue = 550000

print(f"staff with {years_of_experience} years of experience and aged {age} has N{Annual_tax_revenue} Annual tax revenue")

