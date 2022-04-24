import hashlib #модуль хэш функции
from datetime import datetime
import json
from .Service import Techf
from .Transactions import Transaction


class Blockchain:

    chain=[]


    @property
    def last_block():
        return Blockchain.chain[-1]






