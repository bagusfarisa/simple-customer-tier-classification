import tabulate as t


member_plan = {}
member_plan["Platinum"] = {"Discount": 0.15, "Another benefit": "Silver & Gold Tier Benefits + Vacation Voucer + Cashback Up to 30%"}
member_plan["Gold"] = {"Discount": 0.10, "Another benefit": "Silver Tier Benefit + Online TAXI Voucher"}
member_plan["Silver"] = {"Discount": 0.08, "Another benefit": "Food Voucher"}

predict_model = {}
predict_model["Platinum"] = {"Expense": 8, "Income":15}
predict_model["Gold"] = {"Expense": 6, "Income":10}
predict_model["Silver"] = {"Expense": 5, "Income":7}


def show_member_plan():
    for x, y in member_plan.items():
        print(x)
        for z in y:
            print(f"{z}: {y[z]}")
        print()