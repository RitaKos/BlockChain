from .AccountBase import *
from .Blockchain import *
from  .Bank import *
from  .Service import *
from .Transaction import *

class Control:

    @staticmethod
    def validate_transaction(Acount,amount):
        balance=Account.show_account_balance()
        if amount<=balance:
            return True
        else:
            return False

    @staticmethod
    def validate_account(id):
        try:
         index=Account.find_account_index(id)
        except Exception:
            print('ID is not found')
            return False
        else:
            return True

    @staticmethod
    def validate_lake(id):
       try:
           transactions=Transaction.find_transaction_index(id)
       except Exception:
           print('Not completed transactions in the lake is not found')
           return  True
       else:
           print(f'Sender has not compleated transactions: {transactions}')
           return False


