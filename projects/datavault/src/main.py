import csv

with open("projects/datavault/data/raw/transactions.csv", "r") as rt:
    raw_csv = csv.DictReader(rt)

    with open(
        "projects/datavault/data/processed/transactions_processed.csv", "w"
    ) as pt:

        fields = [
            "transaction_id",
            "customer_id",
            "product",
            "quantity",
            "price",
            "date",
            "total_amount",
        ]
        processed_csv = csv.DictWriter(pt, fieldnames=fields)

        processed_csv.writeheader()

        for row in raw_csv:

            row["quantity"] = int(row["quantity"])
            row["price"] = float(row["price"])
            row["total_amount"] = row["quantity"] * row["price"]
            print(row)

            processed_csv.writerow(row)
