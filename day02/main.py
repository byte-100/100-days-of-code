#'hello test from terminal'
#world
#this was done firstly by using the echo to create
#then second to append using the echo "stuff here" >>main.py
#lastly we opened nano to add more text using the inbuilt text editor. 

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

amount =(1 + tip/100) * bill
print(amount)

total_pp = amount/people
total_pp = round(total_pp,2)

print(f"the total per person is ${total_pp}")
