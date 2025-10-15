# Simple ATM console application (demo)
accounts = {'1234': {'pin':'1111','balance':1000}}
def login(acc,pin):
    return acc in accounts and accounts[acc]['pin']==pin
def withdraw(acc,amt):
    if accounts[acc]['balance']>=amt:
        accounts[acc]['balance']-=amt; return True
    return False
if __name__=='__main__':
    acc='1234'; pin='1111'
    if login(acc,pin):
        print('Balance:', accounts[acc]['balance'])
        if withdraw(acc,200):
            print('Withdrawal success. New bal:', accounts[acc]['balance'])
