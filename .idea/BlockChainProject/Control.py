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

    @staticmethod
    def  validateBlockchain():
        prevblock=None
        for block in Blockchain.chain:
            if prevblock:
                actual_prev_hash=Techf.dataToHash(prevblock)
                recorded_prevblock=block['previous_hash']
            if actual_prev_hash != recorded_prevblock:
                print(f"Blockchain is invalid, expected {recorded_prevblock}, actual ={actual_prev_hash}")
            else:
                print(f"Valid hash {actual_prev_hash}")
            prevblock=block

