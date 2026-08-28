import csv
from datetime import datetime


def is_invalid_row(row):

    validity = True
    if len(row["transaction_id"]) == 0:
        validity = False
        msg = "transaction_id is empty"
    elif len(row["customer_id"]) == 0:
        validity = False
        msg = "customer_id is empty"
    elif row["transaction_id"] in set_transaction_id:
        validity = False
        msg = "duplicate transaction_id"

    try:
        quantity = int(row["quantity"])
        if quantity <= 0:
            validity = False
            msg = "quantity is less than 0 or 0"

    except ValueError:
        validity = False
        msg = "quantity is not a number"

    try:
        price = float(row["price"])
        if price < 0:
            validity = False
            msg = "Price is less than 0"

    except ValueError:
        validity = False
        msg = "price is not a number"
    date = row["date"]
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        msg = "Date invalid"
        validity = False
    if not validity:
        row["error_msg"] = msg
        processed_invalid_csv.writerow(row)

    return validity


with open("projects/datavault/data/raw/transactions.csv", "r") as rt:
    raw_csv = csv.DictReader(rt)

    with open(
        "projects/datavault/data/processed/transactions_processed.csv", "w"
    ) as pt:
        with open(
            "projects/datavault/data/processed/invalid_transactions.csv", "w"
        ) as it:

            processed_field = [
                "transaction_id",
                "customer_id",
                "product",
                "quantity",
                "price",
                "date",
                "total_amount",
            ]
            invalid_fields = processed_field + ["error_msg"]
            processed_csv = csv.DictWriter(pt, fieldnames=processed_field)
            processed_invalid_csv = csv.DictWriter(it, fieldnames=invalid_fields)

            processed_csv.writeheader()
            processed_invalid_csv.writeheader()
            set_transaction_id = set()

            customer_spending = {}
            customer_transactions = {}
            product_quantity = {}
            total_transactions = 0
            total_revenue = 0
            Average_transaction_value = 0

            for row in raw_csv:

                validity = is_invalid_row(row)
                # print(validity)
                if validity:

                    set_transaction_id.add(row["transaction_id"])
                    row["quantity"] = int(row["quantity"])
                    row["price"] = float(row["price"])
                    row["total_amount"] = row["quantity"] * row["price"]

                    customer_spending[row["customer_id"]] = (
                        customer_spending.get(row["customer_id"], 0)
                        + row["total_amount"]
                    )

                    customer_transactions[row["customer_id"]] = (
                        customer_transactions.get(row["customer_id"], 0) + 1
                    )

                    total_revenue += row["total_amount"]

                    # Average_transaction_value +=
                    product_quantity[row["product"]] = (
                        product_quantity.get(row["product"], 0) + row["quantity"]
                    )

                    processed_csv.writerow(row)

                else:
                    continue
            highest_spending_customer_value = max(customer_spending.values())
            highest_spending_customer_key = next(
                key
                for key, val in customer_spending.items()
                if val == highest_spending_customer_value
            )

            best_selling_product_value = max(product_quantity.values())
            best_selling_product_key = next(
                key
                for key, val in product_quantity.items()
                if val == best_selling_product_value
            )

            total_transactions = sum(customer_transactions.values())
            Average_transaction_value = total_revenue / total_transactions
            print(f"Total valid transactions: {total_transactions}")
            print(f"Total revenue: {total_revenue}")
            print(f"Average transaction value: {Average_transaction_value}")

            print(f"The highest spending customer is: {highest_spending_customer_key}")

            print(f"The highest spending amount: {highest_spending_customer_value}")

            print(
                f"The best selling product is {best_selling_product_key} with sold value = {best_selling_product_value}"
            )

            print(f"total money spend by each customer :- \n {customer_spending} \n")
            print(
                f"Number of transaction done by each customer:- \n{customer_transactions}\n"
            )
            print(f"number of product sold:- \n {product_quantity}\n")

            print(
                f"The best selling product is {best_selling_product_key} with sold value = {best_selling_product_value}"
            )
