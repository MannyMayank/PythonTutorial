#Classic Hello World
print("Hello World")
#-----------------------------------------------

#Multi line string, use triple quote
print("""Day 1 - Python Print Function
The function is declared like this:
print('what to print')""")
#-----------------------------------------------

#Input Function, take input from console or user
name=input("What is your name?")
print(name)
#-------------------------------------------------

#find length of a string, len()
print("Name is "+str(len(name))+" character long")
#-------------------------------------------------

#Primitive Data Types in Python
# String
# Integer
# Boolean
# Float
#---------------------------------------------------

#Mathematical operators
#3+5
#7-4
#3*2
#6/3
#2**3   => 2*2*2 (exponent)
#orderof calculation is  ()  greater than  **  greater than  */  greater than +-

#Mathematical functions
# round function(roof division) => round(value,number of digit after decimal)
print(round(8/3,2))
#floor division
print(8//3)

#f-string => type f in front of the string before quote
score=0
height=1.8
print(f"your score is {score} , your height is {height}")

#Tip Calculator
print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10,12, or 15? "))
total_people = int(input("How many people to split the bill? "))
each_pay = round((total_bill + (total_bill*(tip_percentage/100)))/total_people,2)
each_pay="{:.2f}".format(each_pay) #format so that it doesn't drop 0 from decimal and restrict to 2 characters
print(f"Each person should pay: ${each_pay}")