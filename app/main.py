# import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop

data = {
    "FUEL_PRICE": 2.4,
    "customers": [
        {
            "name": "Bob",
            "product_cart": {
                "milk": 4,
                "bread": 2,
                "butter": 5
            },
            "location": [12, -2],
            "money": 55,
            "car": {
                "brand": "Suzuki",
                "fuel_consumption": 9.9
            }
        },
        {
            "name": "Alex",
            "product_cart": {
                "milk": 2,
                "bread": 2,
                "butter": 2
            },
            "location": [1, -2],
            "money": 41,
            "car": {
                "brand": "BMW",
                "fuel_consumption": 9.1
            }
        },
        {
            "name": "Monica",
            "product_cart": {
                "milk": 3,
                "bread": 3,
                "butter": 1
            },
            "location": [11, -2],
            "money": 12,
            "car": {
                "brand": "Audi",
                "fuel_consumption": 7.6
            }
        }
    ],
    "shops": [
        {
            "name": "Outskirts Shop",
            "location": [10, -5],
            "products": {
                "milk": 3,
                "bread": 1,
                "butter": 2.5
            }
        },
        {
            "name": "Shop '24/7'",
            "location": [4, 3],
            "products": {
                "milk": 2,
                "bread": 1.5,
                "butter": 3.2
            }
        },
        {
            "name": "Central Shop",
            "location": [0, 0],
            "products": {
                "milk": 3,
                "bread": 2,
                "butter": 3.5
            }
        }
    ]
}


def shop_trip() -> None:
    # with open("config.json", "r") as file:
    #     data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    customers = [
        Customer(customer["name"], customer["money"], customer["location"],
                 Car(customer["car"]["brand"],
                     customer["car"]["fuel_consumption"],
                     customer["location"]), customer["product_cart"])
        for customer in data["customers"]]

    shops = [Shop(shop["name"], shop["products"], shop["location"])
             for shop in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shopping = customer.find_the_cheapest_shopping(
            shops, fuel_price)

        if cheapest_shopping[1] <= customer.money:
            customer.make_shopping(cheapest_shopping[0], fuel_price)
        else:
            print(f"{customer.name} doesn't have enough money to "
                  + "make a purchase in any shop")
