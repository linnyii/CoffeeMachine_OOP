class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUE = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money:{self.profit}{self.CURRENCY}")

    def process_coins(self):
        print("please insert coins")
        for coin in self.COIN_VALUE:
            self.money_received += int(input(f"How many {coin}?")) * self.COIN_VALUE[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"here is {change} in change")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("sorry, the money is not enough. payment is refunded")
            return False
