#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator!\n")

total_bill = float(input("What was the total bill? $ "))

tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

num_people = int(input("How many people to split the bill? "))

tip_amount = total_bill *(tip_percentage/100)

final_bill = total_bill + tip_amount

bill_per_person = round(final_bill/num_people, 2)

print(f"Each person should pay: ${bill_per_person}\n")

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
