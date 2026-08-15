india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Write a program that asks user to enter a city name and it should
# tell which country the city belongs to

user_input = input("Enter city name: ")

if user_input in india:
    print(f"{user_input} is an Indian city.")
elif user_input in pakistan:
    print(f"{user_input} is a Pakistani city.")
elif user_input in bangladesh:
    print(f"{user_input} is bangladeshi city.")
else:
    print("City not found for a given lists")

# Write a program that asks user to enter two cities and it tells you if
# they both are in same country or not. For example if I enter mumbai
# and chennai, it will print "Both cities are in India" but
# if I enter mumbai and dhaka it should print "They don't belong to same country"

user_input_1 = input("Enter first city name: ")
user_input_2 = input("Enter second city name: ")

if user_input_1 in india and user_input_2 in india:
    print("Both cities are in India")

elif user_input_1 in pakistan and user_input_2 in pakistan:
    print("Both cities are in Pakistan")

elif user_input_1 in bangladesh and user_input_2 in bangladesh:
    print("Both cities are in Bangladesh")

else:
    print("They don't belong to same country")
