from .AccountBase import *
from .Blockchain import *
from  .Bank import *
from  .Service import *


class Transaction(object):
    def __int__(self):
        self.transaction={
            'from': sender,
            'to': recipient,
            'amount': amount,
        }
    transaction_lake=[]

    @staticmethod
    def find_transaction_index(user_id):
        index=next((num for num,number in enumerate(Transaction.transaction_lake) if number['from']==user_id),None)
        return index

    @staticmethod
    def newtransaction(sender,recipient,amount):
         newtrans=self.transaction
         self.transaction_lake.append(newtrans)



