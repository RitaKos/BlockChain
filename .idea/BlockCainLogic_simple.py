import hashlib #модуль хэш функции
from random import randint
from datetime import datetime
import json


# accounts base is empty
users_accounts_base=[];

# blockchain. Let's start with first empty block
blockchain=[];
e_block={
    'from': '',
    'to': '',
    'amount': 0.0
}
blockchain.append(e_block);

# function defines index of account you need
def find_account_index(user_id):
    x=next((num for num,numer in enumerate(users_accounts_base) if number['user_id']==user_id),None)
    return x

# function for hash generating
def dataToHash(data):
    json_data=json.dumps(data,sort_keys=True) # convert dictionary to string
    binary_data=json_data.encode() # convert string to binary data
    return hashlib.sha256(binary_data).hexdigest()

# creating a new account funtion
def create_accout(name,surname):
 prev_block=blockchain[-1]
 prev_hash=dataToHash(prev_block)

 balance=0.0;
 user_id=randint(1,1000000000)
 activation_date =str(datetime.now())
 user_account={
    'user_id': user_id,
    'name': name,
    'surname': surname,
    'balance': balance,
    'open_date': activation_date
 }
 activation_block={   # add new block to the blockchain
     'from': user_id,
     'to': user_id,
     'amount': 0.0,
     'prev_hash': prev_hash
 }

 users_accounts_base.append(user_account)
 blockchain.append(activation_block)
 return user_account

# adding coins to account
def add_balance(user_id,amount):
   prev_block=blockchain[-1]
   prev_hash=dataToHash(prev_block)
   x= find_account_index(user_id)
   users_accounts_base[x]['balance']=users_accounts_base[x]['balance'] + amount
   transaction_block={  # add new block to the blockchain
    'from': user_id,
    'to': user_id,
    'amount': amount,
    'prev_hash': prev_hash
   }
   blockchain.append(transaction_block)


# show account balance
def show_balance_info(user_id):
    x=find_account_index(user_id)
    current_balance=users_accounts_base[x]['balance']
    print(current_balance)
    return current_balance


# money transaction to another account

def send_money(sender,recipient,amount):
    prev_block=blockchain[-1]
    prev_hash=dataToHash(prev_block)
    a=find_account_index(sender)
    b=find_account_index(recipient)
    users_accounts_base[a]['balance']=users_accounts_base[a]['balance'] - amount
    users_accounts_base[b]['balance']=users_accounts_base[b]['balance'] + amount
    transaction_block={  # add new block to the blockchain
        'from': sender,
        'to': recipient,
        'amount': amount,
        'prev_hash': prev_hash
    }
    blockchain.append(transaction_block)

# Proof

def isValidateProof(block,proof): #подходит ли число в качестве до-ва работы
    block_copy=block.copy() #копируем блок
    block_copy['proof'] = proof
    hash= dataToHash(block_copy)  # считаем новый хэш
    is_valid_hash = hash[0:3] =='000'
    if is_valid_hash:
        print(hash)
    return is_valid_hash # начинается ли хэш с нулей как тебуется

# Mining

def mineProofOfWork(block): # майним число , которое подставим к блоку , и хэш будет начинаться с 2 нулей
    proof = 0
    while not isValidateProof(block,proof):
        proof+=1
    return  proof


# Validation
print(create_accout('Nick','Oren'))
print(create_accout('Tom','Rid'))
#add_balance(608244938,87)
id_ran=users_accounts_base[0]['user_id']
add_balance(id_ran,800.0)
add_balance(id_ran,300.0)
print(users_accounts_base)
show_balance_info(id_ran)
print(blockchain)
id_ran_2=users_accounts_base[-1]['user_id']
send_money(id_ran,id_ran_2,150.0)
print(blockchain)
mineProofOfWork(blockchain[0])

