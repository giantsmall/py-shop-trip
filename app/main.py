import jsonfrom app.customer import Customerfrom app.shop import Shopdef shop_trip():    print("json")    json_content = json.load(open("config.json","r"))    print(json_content)    fuel_price = json_content["FUEL_PRICE"]    customers_data = json_content["customers"]    customers = []    for cust_data in customers_data:        customers.append(Customer(cust_data))    shops = []    for shop_data in json_content["shops"]:        shops.append(Shop(shop_data))    cheapest_shop: Shop    lowest_cost = 99999    for customer in customers:        print(f"{customer.name} has {customer.money} dollars")        for shop in shops:            travel_cost = customer.location.calculate_distance(shop.location) * customer.car.fuel_consumption / 100.0 * fuel_price            shopping_cost = shop.calculate_shopping(customer)            total_cost = round(shopping_cost + travel_cost, 2)            print(f"{customer.name}'s trip to {shop.name} costs {total_cost}")            if total_cost < lowest_cost:                lowest_cost = total_cost                cheapest_shop = shop        if customer.money >= lowest_cost:            print(f"{customer.name} rides to {cheapest_shop.name}\n")            cheapest_shop.make_shopping(customer)            print(f"{customer.name} rides home")            print(f"{customer.name} now has {customer.money} dollars\n")        else:            print(f"{customer.name} doesn't have enough money to make a purchanse in any shop")shop_trip()