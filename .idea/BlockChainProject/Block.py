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
            'previous_hash': prevhash,
            'voits': 0
        }
        block['proof']=Blockchain.mineProofOfWork(block)
        Blockchain.chain.append(block)
        return block

    # Validate block for consensus voiting
    def blockVoiting(self):
        if Control.validateBlockchain():
            self['voits']= self['voits']+1
        else: return False

    # Validate proof
    def isValidateProof(self,proof): #подходит ли число в качестве до-ва работы
        block_copy=self.copy() #копируем блок
        block_copy['proof'] = proof
        hash= Techf.dataToHash(block_copy)  # считаем новый хэш
        is_valid_hash = hash[0:3] =='000'
        if is_valid_hash:
            print(hash)
        return is_valid_hash # начинается ли хэш с нулей как тебуется

    # Mining
    def mineProofOfWork(self):
        proof = 0
        while not isValidateProof(self,proof):
            proof+=1
        return proof