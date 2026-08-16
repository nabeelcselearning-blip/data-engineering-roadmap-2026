stocks_price = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160],
}


def print_method():
    for key, value in stocks_price.items():
        # print(value)
        avg = sum(value) / len(value)
        print(f"{key} ==> {value} ==> avg: {avg:.2f} ")


def add():
    ticker = input("Enter Ticker name: ")
    price = int(input("Enter price: "))
    if ticker in stocks_price:
        stocks_price[ticker].append(price)
        print_method()
    else:
        stocks_price[ticker] = [price]
        print_method()


print("Enter Your Choice:")
print("1.print: print stocks prices record")
print("2.add: to add more records in data base")

user_input = input("Write your input here: ")

match user_input:
    case "print":
        print_method()
    case "add":
        add()
