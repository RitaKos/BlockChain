import hashlib #модуль хэш функции
from datetime import datetime
from random import randint
import json
import  getpass
import sys
from .Service import Techf
from .Control import Control

# Account base conains accounts of blockchain users. For creating we don't need any personal data
# as wel as contact information. All transaction is available by using ID and Key. For generating personal key
# user shoud provide string key before 100 and 300 letters( it may be sentence).
# Removing existed account is not available.
# Recovery personal key is possible just if you know string key with all registers.

class Account(object):
    def __int__(self):
        self.user_account={}

# List of existed accounts
    users_account_base=[]

# create account
    def create_account(self,inner_key):
      if 300<len(inner_key)>100:
        balance=0.00;
        user_id=Techf.id_generation()
        activation_date =str(datetime.now())
        _key_unique = Techf.KeyDataToHash(inner_key)
        user_account={
            'user_id': user_id,
            'key': _key_unique,
            'string_key': inner_key,
            'balance': balance,
            'open_date': activation_date
        }
        self.user_account =user_account
        self.users_account_base.append(user_account)
      else:
          print('String key doesn\'t match requirements about it\'s length.')
      return user_account

# show account info
    def account_info(self):
        print(f"""ID: {self.user_account['user_id']} \nBalance: {self.user_account['balance']}\nActivation date: {self.user_account['open_date']}""")

# show account balance
    def show_account_balance(self):
        return self.user_account['balance']

    def replenish_balance(self,amount):
        curr_balance=self.show_account_balance()
        new_balance=curr_balance+amount
        self.user_account['balance']=new_balance
        return new_balance

# function for geting Accont index from Account Base by user_id
    def find_account_index(self,user_id):
        index=next((num for num,number in enumerate(self.users_account_base) if number['user_id']==user_id),None)
        return index


# validate key
    def pass_validating(self):
        pwd=getpass.getpass(prompt='Enter your key')
        if pwd ==self.user_account['key']:
             print('Welcome')
             access = True
        else:
            print('Key is incorrect')
            access = False
        return access


# Enter in account
    def enter_account(self, id):
        index= self.find_account_index(id)
        if self.users_account_base[index]['user_id']==id:
            access=self.pass_validating()
            if access == True:
                self.account_info()
            else:
                print('Permitted access. Key is wrong!')
        else:
            print('Permitted access. Account with such ID is not found.')
        return access

# key recovery by string key
    def recover_key(self,inner_key):
        attempts=0
        while attempts<1:
            if self.user_account['string_key']==inner_key:
                print(self.user_account['key'])
                quit()
            else:
                print('Secret password is incorrect, try another one after 24 hours')
                attempts+=1

# make new transaction
    def new_transaction(self,recipient,amount):
        if Control.validate_transaction(self,amount):
           if Control.validate_account(recipient):
               if Control.validate_lake(self.user_account['user_id']):




if __name__ == '__main__':

 acc_1=Account()
 print(acc_1.create_account('Happy day'))
 acc_1.account_info()
 #acc_1.recover_key('Happy 2 day')
 #print(Account.users_account_base)
 id_ran=Account.users_account_base[0]['user_id']
 acc_1.enter_account(id_ran)



