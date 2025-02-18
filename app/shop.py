from datetime import datetime
from app.customer import Customer
from app.point import Point


class Shop:
    def __init__(self, shop_data):
        self.name = shop_data["name"]
        self.location = Point(shop_data["location"])
        self.products = shop_data["products"]

    def calculate_shopping(self, customer: Customer) -> float:
        total_price = 0
        for item in customer.product_cart.keys():
            total_price += self.products[item] * customer.product_cart[item]
        return total_price

    def make_shopping(self, customer: Customer) -> None:
        total_cost = 0
        date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"Date: {date_str}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for item in customer.product_cart.keys():
            amount = customer.product_cart[item]
            position_price = self.products[item] * amount
            total_cost += position_price
            print(f"{amount} {item}s for {position_price} dollars")

        #print(f"{customer.money - total_cost} = {customer.money} - {total_cost}")
        customer.money -= total_cost
        print(f"Total cost is {total_cost} dollars")
        print(f"See you again!\n")
