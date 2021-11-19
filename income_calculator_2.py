#Requires User to press enter to start the program
print('')
input("Welcome, this machine calculates your actual annual, monthly, and weekly income after taxes! \nPlease press *Enter* to start! ")

#Requires User to enter their marital status
print('')
marital_status = input("First, please enter your marital status:\n**(S)** Single\n**(M)** Married\n-> ").upper()

#------------------------------------------------------------------------
#This section of code runs a while loop to ensure the user inputs the correct input (S) or (M) for mariatl status
#When the user inputs (S) or (M), they will tax their income by the corresponding tax brackets
#There loop also makes sure the user inputs their marital status correctly or will ask again because it's invalid
#REFERENCE - Tax Bracket from https://www.johndaviscpa.com/taxrates2.php


while True:
    if marital_status == "S":    
        if gross_annual_income <= 9950:
            tax = 0.10
        elif gross_annual_income > 9950 and gross_annual_income <= 40525:
            tax = 0.12
        elif gross_annual_income > 40525 and gross_annual_income <= 86375:
            tax = 0.22
        elif gross_annual_income > 86375 and gross_annual_income <= 164925:
            tax = 0.24
        elif gross_annual_income > 164925 and gross_annual_income <= 209425:
            tax = 0.32
        elif gross_annual_income > 209425 and gross_annual_income <= 518400:
            tax = 0.35
        elif gross_annual_income > 518400:
            tax = 0.37    
        break

    elif marital_status == "M":
        if gross_annual_income <= 19900:
            tax = 0.10
        elif gross_annual_income > 19900 and gross_annual_income <= 81050:
            tax = 0.12
        elif gross_annual_income > 81050 and gross_annual_income <= 172750:
            tax = 0.22
        elif gross_annual_income > 172750 and gross_annual_income <= 329850:
            tax = 0.24
        elif gross_annual_income > 329850 and gross_annual_income <= 418850:
            tax = 0.32
        elif gross_annual_income > 418850 and gross_annual_income <= 628300:
            tax = 0.35
        elif gross_annual_income > 628300:
            tax = 0.37    
        break

    else:
        marital_status = input("Invalid choice: please enter your marital status:\n**(S)** Single\n**(M)** Married\n-> ").upper() 
        continue


#Requires User to enter pay and hours weekly or salary
print('')
income = input("Please select the mode to calculate your actual income:\n**(1)** pay/hours per week\n**(2)** annual salary\n-> ")


#------------------------------------------------------------------------
#This loop makes sure the user inputs "1" or "2" in order to calculate the users income 
#If the user does not put in the correct input, it will say its an invalid input and it will loop until it gets a 1 or 2
#Input "1" calculates the user's income by hourly pay and hours per week
#Input "2" calculates the user's income from annual salary

while True:
    
    if income == "1":
        print('')
        print("Please enter your hourly pay and hours per week:")
        pay = int(input("Hour pay: "))
        hours = int(input("Hours per week: "))
        gross_annual_income = (pay * hours) * 56
        break

    elif income == "2":
        print('')
        gross_annual_income = int(input("Please enter your annual salary: "))
        break

    elif income != "1" or income != "2":
        income = input("Invalid choice: Please select:\n**(1)** pay/hours per week\n**(2)** annual salary\n-> ") 
        continue

#------------------------------------------------------------------------
#These are the equations that will calculate the users income before and after taxes  
taxed_income = gross_annual_income * tax 
annual_income = gross_annual_income - taxed_income
weekly_income = annual_income / 56
monthly_income = annual_income / 12

#------------------------------------------------------------------------
#These will be the outputs showing the user their income before and after taxes
print("\nYour actual income per year, month, and week is:")
print("\n**Income BEFORE taxes**")
print(f"Gross annual income: ${gross_annual_income}")
print("\n**Income AFTER taxes**")
print(f"Annual income: ${int(annual_income)}")
print(f"Monthly income: ${int(monthly_income)}")
print(f"Weekly income: ${int(weekly_income)}")
print('\n')