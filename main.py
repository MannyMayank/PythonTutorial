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