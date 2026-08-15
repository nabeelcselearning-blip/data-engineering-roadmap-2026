# Create a variable called break and assign it a value 5. See what happens and find out the reason behind
# the behavior that you see.

# break = 5

# ANSWER: Syntax error(invalid syntax) will occur, bcz it is a reserved keyword used in python to get out of the loop.


# QUESTION 2:
# Create two variables. One to store your birth year and another one to store current year.
# Now calculate your age using these two variables

birth_year = 2000
current_year = 2026
age = current_year - birth_year
print(age)

# QUESTION 3:
# Store your first, middle and last name in three different variables and then
# print your full name using these variables

first_name = "Nabeel"
last_name = "Islam"
print(first_name + " " + last_name)

# QUESTION 4:
# Answer which of these are invalid variable names:
# _nation, 1record, record1, record_one, record-one, record^one, continue

# ANSWER
# 1. _nation is valid   (only _ is also valid and we used in for loops)
# 2. 1record is not valid   (we cannot use digits at first place but can be used in bwetween or in last)
# 3. record1 is valid   (we can use digits anywhere in variable name except at first pos)
# 4. record_one is valid
# 5. record-one is not valid we cannot use - anywhere in variable name.
# 6. record^one is not valid as we cannot use ^ anywhere in variable name.
# 7. continue is not valid (it can be used only within a loop) it is a reserved keyword
