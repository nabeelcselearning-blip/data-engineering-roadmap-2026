# SOLUTION 1:
result = [
    "heads",
    "tails",
    "tails",
    "heads",
    "tails",
    "heads",
    "heads",
    "tails",
    "tails",
    "tails",
]

count_heads = 0
for elem in result:
    if elem == "heads":
        count_heads += 1

print(f"We got {count_heads} times heads")


# SOLUTION 2:
for i in range(11):
    if i % 2 != 0:
        print(i**2, end=" ")

print()
# SOLUTION 3:
expense_list = [2340, 2500, 2100, 3100, 2980]
expense_amount = int(input("Enter an expense amount: "))

cond = False
month = ""
for i in range(5):
    if expense_list[i] == expense_amount:
        cond = True
        if i == 0:
            month = "January"
        elif i == 1:
            month = "February"
        elif i == 2:
            month = "March"
        elif i == 3:
            month = "April"
        else:
            month = "May"
        break
if cond:
    print(f"{expense_amount} spend in {month}")
else:
    print(f"{expense_amount} is not spend from January to May")

# SOLUTION 4:

tired = False
for i in range(5):
    prompt = input("Are you tired?")
    if prompt == "yes":
        print("you didn't finish the race")
        tired = True
        break
if not tired:
    print("Congratulations u completed the race")

# SOLUTION 5:

for i in range(5):
    for j in range(0, i + 1):
        print("*", end="")

    print()
