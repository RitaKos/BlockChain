import hashlib #модуль хэш функции
from datetime import datetime
import json
from .Service import Techf


class Blockchain(object):
    def __int__(self):
        self.chain=[]
        self.current_transactions=[]

    @property
    def last_block(self):
        return self.chain[-1]

    def new_block(self,proof,previous_hash=None):
        block={   # add new block to the blockchain
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_transactions=[]
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        transaction={   # add new transaction to the block
            'from': sender,
            'to': recipient,
            'amount': amount,
        }
        self.current_transactions.append(transaction)
        return  self.last_block['index']+1





