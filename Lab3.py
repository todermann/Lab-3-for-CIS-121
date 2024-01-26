'''

This function will take two inputs, Earned Income and Martial Status.
And print the amount of taxes owed for the 2023 year based on these two inputs.

'''

single_adding_lower = 1100

single_adding_mid = 4046.88

married_adding_lower = 2200

married_adding_mid = 8093.88

marital_status = input("Enter Marital Status for 2023: ")


if marital_status not in ["single", "married"] :
	print("Unfortunately, this calculator is not built for you!")

earned_income = int(input("Enter Earned Income For 2023: "))
	
if marital_status == "single" and earned_income > 95375 :
	print("This calculator will not work in your circumstance because you made too much mula!")
	
elif marital_status == "married" and earned_income > 190750 :
	print("This calculator will not work in your circumstance because you made too much mula!")

elif marital_status == "single" and earned_income in range (0, 11001) :
	single_taxes_due = earned_income * 0.10
	print("Your taxes owed for 2023 are")
	print(single_taxes_due)
	
elif marital_status == "single" and earned_income in range (11001, 44726) :
	single_mid_tax = (earned_income - 11000) * 0.12
	single_mid_tax = single_adding_lower + single_mid_tax
	print("Your taxes owed are")
	print(single_mid_tax)
	
elif marital_status == "single" and earned_income > 44726 :
	single_upper_tax = (earned_income - 44725) * 0.22
	single_upper_tax = single_adding_lower + single_adding_mid + single_upper_tax
	print("Your taxes owed are")
	print(single_upper_tax)
	
elif marital_status == "married" and earned_income in range (0, 22001) :
	married_taxes_due = earned_income * 0.10
	print("Your taxes owed are")
	print(married_taxes_due)

elif marital_status == "married" and earned_income in range (22001, 89451) :
	married_mid_tax = (earned_income - 22000) * 0.12
	married_mid_tax = married_adding_lower + married_mid_tax
	print("Your taxes owed are")
	print(married_mid_tax)

elif marital_status == "married" and earned_income > 89451 :
	married_upper_tax = (earned_income - 89450) * 0.22
	married_upper_tax = married_adding_lower + married_adding_mid + married_upper_tax
	print("Your taxes owed are")
	print(married_upper_tax)

