from .AccountBase import *
from .Blockchain import *

class Bank(object):
    def __int__(self):
        self.coin_demand=0.00
        self.coin_offer=0.00
        self.currency_list=['USD','EUR','RUB']
        self.currency_price={'USD':0,'EUR':0,'RUB':0}
        self.currency_storage={'USD':0,'EUR':0,'RUB':0}
        self.coin_storage=1000000

# Buying coins for currency
    def buy_coin(self,id,currency,amount):
        buyer = Account.find_account_index(id)
        buyer_balance=Account.show_account_balance(buyer)
        for item in self.currency_price.keys():
            if item==currency:
                course=self.currency_price.values(item)
            else:
                print('Currency is not defined')
                quit()
        for unit in self.currency_storage.keys():
            if unit==currency:
                quality=self.currency_storage.values(unit)
                new_quality=quality+amount
                self.currency_storage[unit]=new_quality
            else:
                print('Currency is not defined in storage')
                block_currency={currency:amount}
                return block_currency
                quit()
        coins_amount=course*amount
        Account.replenish_balance(buyer,coins_amount)
        self.coin_demand=self.coin_demand+coins_amount
        return self.coin_demand

# Convert coins to currency
    def convert_coin(self,id,amount,currency):
        seller = Account.find_account_index(id)
        seller_balance=Account.show_account_balance(seller)
        for item in self.currency_price.keys():
            if item==currency:
                course=self.currency_price.values(item)
            else:
                print('Currency is not defined')
                quit()
        for unit in self.currency_storage.keys():
            if unit==currency:
                quality=self.currency_storage.values(unit)
                new_quality=quality-amount
                self.currency_storage[unit]=new_quality

            else:
                print('Currency is not defined in storage')
                request_currency={currency:amount}
                return request_currency
                quit()
        coins_amount=course*amount*(-1)
        Account.replenish_balance(buyer,coins_amount)
        self.coin_demand=self.coin_demand-coins_amount
        return self.coin_demand

# Get currency price
    def show_currency_price(self):
        print(f'Current currency price info: {self.currency_price}')