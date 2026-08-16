country_population = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}

user_input = input()

if user_input == "print":
    for key, value in country_population.items():
        print(f"{key} ==> {value}")

elif user_input == "add":
    country = input("Enter Country Name: ")  # case sensitive India != india
    if country not in country_population:
        population = int(input("Enter population"))
        country_population[country] = population
    else:
        print("It already exists")

elif user_input == "remove":
    country = input("Enter Country Name: ")
    if country in country_population:
        del country_population[country]
    else:
        print("Country doesn't exist")
elif user_input == "query":
    country = input("Enter Country Name to Query: ")
    if country in country_population:
        print(f"The population of {country} is: {country_population[country]}")
