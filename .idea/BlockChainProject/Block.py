import hashlib #модуль хэш функции
from datetime import datetime
import json
from .Service import Techf
from .Transactions import Transaction
from .Blockchain import *
from .Blockchain import mineProofOfWork
from .Blockchain import isValidateProof

class Block(object):
    def __int__(self):
        self.block={}


    # new block creating
    def newblock(self):
        index=len(Blockchain.chain)+1
        blocktrans=Transaction.transaction_lake.pop(0,1,2,3,4,5,6,7,8,9)
        prevhash=Techf.dataToHash(Blockchain.chain[-1])
        block={
            'index': index,
            'timestamp': time(),
            'transactions': blocktrans,
            'proof': proof,
            'previous_hash': prevhash
        }
        block['proof']=Blockchain.mineProofOfWork(block)
        Blockchain.chain.append(block)
        return block

