import hashlib #модуль хэш функции
from datetime import datetime
import json
from .Service import Techf
from .Transactions import Transaction


class Blockchain(object):
    def __int__(self):
        self.chain=[]

# new block creating
    def newblock(self,transactions,proof):
        block={
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions': Transaction.transaction_lake[:10],
            'proof': proof,
            'previous_hash': Techf.dataToHash(self.chain[-1])
        }
        self.chain.append(block)
        return block

#Proof
@staticmethod
def isValidateProof(block,proof): #подходит ли число в качестве до-ва работы
    block_copy=block.copy() #копируем блок
    block_copy['proof'] = proof
    hash= Techf.dataToHash(block_copy)  # считаем новый хэш
    is_valid_hash = hash[0:3] =='000'
    if is_valid_hash:
        print(hash)
    return is_valid_hash # начинается ли хэш с нулей как тебуется

# validate block
def  validateBlockchain(self):
    prevblock=None
    for block in self.chain:
        if prevblock:
            actual_prev_hash=Techf.dataToHash(prevblock)
            recorded_prevblock=block['previous_hash']
        if actual_prev_hash != recorded_prevblock:
            print(f"Blockchain is invalid, expected {recorded_prevblock}, actual ={actual_prev_hash}")
        else:
            print(f"Valid hash {actual_prev_hash}")
        prevblock=block

# Mining
@staticmethod
def mineProofOfWork(block):
    proof = 0
    while not isValidateProof(block,proof):
        proof+=1
    return proof

    @property
    def last_block(self):
        return self.chain[-1]
        #return  self.last_block['index']+1





