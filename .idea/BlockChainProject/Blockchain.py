import hashlib #модуль хэш функции
from datetime import datetime
import json
from .Service import Techf
from .Transactions import Transaction


class Blockchain:

    chain=[]

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

# Mining
    @staticmethod
    def mineProofOfWork(block):
        proof = 0
        while not isValidateProof(block,proof):
            proof+=1
        return proof

    @property
    def last_block():
        return Blockchain.chain[-1]






