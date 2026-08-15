# a. Ask user to enter his fasting sugar level

fasting_sugar = int(input("Enter fasting sugar level: "))

if fasting_sugar < 80:
    print("Sugar is low")
elif fasting_sugar > 100:
    print("Sugar is high")
else:
    print("Sugar is normal")
