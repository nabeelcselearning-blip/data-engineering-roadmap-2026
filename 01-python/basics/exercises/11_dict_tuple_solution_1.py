country_population = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}


def print_method():
    for key, value in country_population.items():
        print(f"{key} ==> {value}")


def add():
    country = input("Enter Country Name: ")  # case sensitive India != india
    if country not in country_population:
        population = int(input("Enter population"))
        country_population[country] = population
        print(f"{country} ==> {population}")
    else:
        print("It already exists")


def remove():
    country = input("Enter Country Name: ")
    if country in country_population:
        del country_population[country]
        print_method()
    else:
        print("Country doesn't exist")


def query():
    country = input("Enter Country Name to Query: ")
    if country in country_population:
        print(f"The population of {country} is: {country_population[country]}")
    else:
        print("country not found.")


print(
    "Enter Your Choice:\n1.print: to print dict\n2.add: to add more country records.\n3.remove: to remove a country record.\n4.query to query from existing records. "
)
user_input = input()

match user_input:
    case "print":
        print_method()

    case "add":
        add()

    case "remove":
        remove()

    case "query":
        query()

    case _:
        print("Invalid Input")
