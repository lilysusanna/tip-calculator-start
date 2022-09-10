#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator.")
bill=float(input("What is the total bill? $"))
tip1=int(input("What percentage tip would you like to give? 10, 12 or 15? $"))
split=int(input("How many people to split bill? "))
tip=bill*(tip1/100)
Tbill=(bill+tip)/split
Tbill=round(Tbill, ndigits=2)
print(f"Each person should pay ${Tbill}")