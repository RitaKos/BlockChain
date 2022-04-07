

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

    def new_transaction():