# QUESTION 1
"""
Create 3 variables to store street, city and country, now create address variable to store entire address.
Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line
"""

street = "Palminton"
city = "Newyork"
country = "USA"

address1 = street + " " + city + " " + country + "."
address2 = f"{street} {city} {country}."
print(address1)
print(address2)

print(f"{street} \n{city} \n{country}")  # using each variable
print(f"{address1[0:10]} \n{address1[10:18]} \n{address1[18:-1]}")  # using slicing

# QUESTION 2:
"""
Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index
"""
string = "Earth revolves around the sun"
print(string[6:14])
print(string[-3:])

# QUESTION 3
"""
Create two variables to store how many fruits and vegetables you eat in a day.
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
Use python f string for this.
"""

vegi = 3
fruits = 6

print(f"I eat {vegi} veggies and {fruits} fruits daily.")

# QUESTION 4

"""
I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement,
the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original string 
with new ones and print the new string. Also try to do this in one line.
"""

s = "maine 200 banana khaye"
print(s.replace("200 banana", "10 samosa"))
