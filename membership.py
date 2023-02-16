import math


tier_name = ["Platinum", "Gold", "Silver"]
tier_discount = [0.25, 0.15, 0.10]
tier_requirement = ["Buy item(s) worth of 1,000,000 IDR",
                    "Buy item(s) worth of 500,000 IDR",
                    "Buy item(s) worth of 100,000 IDR"] 

predict_model = [["Platinum", "Gold", "Silver"],
                [4000000, 2000000,1000000],
                [8000000,5000000,3000000]]


def show_all_offer():
    n = 0
    while n < len(tier_name):
        print(tier_name[n])
        print(f"Discount: {tier_discount[n]}")
        print(f"Requirement: {tier_requirement[n]}")
        print()
        n += 1


def show_offer(tier_name):
    print(tier_name)
    index = tier_name.index(tier_name)
    print(f"Discount: {tier_discount[index]}")
    print(f"Requirement: {tier_requirement[index]}")


def predict_tier(expense, income):
    euclid_distance = []
    n = 0
    while n < len(tier_name):
        x = math.sqrt((expense - predict_model[1][n])**2 + (income - predict_model[2][n])**2)
        euclid_distance.append(x)
        n += 1
    min = euclid_distance[0]
    index = 0
    for i in range(1, len(euclid_distance)):
        if euclid_distance[i] < min:
            min = euclid_distance[i]
            index = i
    customer_tier = tier_name[index]
    return customer_tier
