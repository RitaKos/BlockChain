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
                    return False
                else:
                    print(f"Valid hash {actual_prev_hash}")
                    prevblock=block
                    return  True



    @staticmethod
    def consensus(block):
        if block['voits']>100 :  # temporary decision
            succestrans=block['transactions']
            for trans in succestrans:
                id_s=trans['sender']
                id_r = trans['recipient']
                index_s=Account.find_account_index(id_s)
                index_r=Account.find_account_index(id_r)
                sender=Account.users_account_base[id_s]
                recipient=Account.users_account_base[id_r]
                sender['frozzen']=sender['frozzen']-trans['amount']
                sender['balance']= sender['balance']-trans['amount']
                recipient['balance']= recipient['balance']+trans['amount']
                return True
            else:
                return False