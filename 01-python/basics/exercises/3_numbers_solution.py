# QUESTION 1
# You have a football field that is 92 meter long and 48.8 meter wide.
# Find out total area using python and print it.

length = 92
width = 48.8
total_area = length * width
print(total_area)
print(
    round(total_area, 3)  # round ignores trailing zeros after the decimal.
)  # it will round the result but what If you want exactly 3 digits after the decimal
print(f"{total_area:.3f}")


# QUESTION 2
# You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
# and you gave shopkeeper 20 dollar. Find out using python,
# how many dollars is the shopkeeper going to give you back?

no_packets = 9
cost_of_each_packet = 1.49
money_given_by_you = 20
shopkeeper_return = money_given_by_you - no_packets * 1.49
print(shopkeeper_return)

# QUESTION 3
# You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

length_tiles = 5.5
cost_of_tiles_per_sqft = 500

area_of_bathroom = length_tiles**2
total_cost = cost_of_tiles_per_sqft * area_of_bathroom
print(total_cost)

# QUESTION 4
# Print binary representation of number 17

number = 17
print(bin(number))
