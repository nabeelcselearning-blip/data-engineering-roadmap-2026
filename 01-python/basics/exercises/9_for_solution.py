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

print(f"We gor {count_heads} times heads")


# SOLUTION 2:
for i in range(11):
    if i % 2 != 0:
        print(i**2, end=" ")
