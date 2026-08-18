import csv

with open("projects/datavault/data/raw/transactions.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:

        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        row["total_amount"] = row["quantity"] * row["price"]
        print(row)
