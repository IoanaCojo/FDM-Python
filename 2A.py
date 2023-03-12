"""
Class Activity
"""
from itertools import count


class BankAccount():
    no_accounts = 0
    def __init__(self, acc_no, sort_code, name, amount):
        self.acc_no = acc_no
        self.sort_code = sort_code
        self.name = name
        self.balance = amount
        self.transaction = []
        self.__class__.no_accounts +=1

    def print_message(self):
        print(f"New bank account opened for {self.name}")


    def get_balance(self):
        return self.balance


    def set_balance(self, amount):
        self._balance = amount
        print(f'{self._balance}  can be changed with {amount}')


    def get_acc_no(self):
        return self.acc_no


    def set_acc_no(self, new_acc_no):
        print(f'The previous acc_no {self.acc_no} will change to {new_acc_no}')
        self.acc_no = new_acc_no


    def get_sort_code(self):
        return self.sort_code


    def set_sort_code(self, new_sort_code):
        print(f'The previous acc_ no {self.sort_code} will change to {new_sort_code}')
        self.sort_code = new_sort_code


    def get_transaction(self):
        return self.transaction

    def __delete__(self):
        print(f'the bank account {self.name}: {self.acc_no} : {self.sort_code} has been deleted')
        self.__class__.no_accounts -=1

    def make_transaction(self,trans_amount):
        if type(trans_amount) is int or type(trans_amount) is float:
            self.balance = self.balance + trans_amount
            self.transaction.append('+') if trans_amount > 0 else ''

            self.transaction.append(trans_amount)
            print(f'successful transaction')
        else:
            print(f'trans_amount must be an integer or a float number')

    def num_transactions(self):
        return len(list(filter(lambda trans: type(trans) == int or type(trans) == float, self.transaction)))






first_BA= BankAccount(123,11111,'Andrei',100)
print(first_BA.get_balance())

second_BA= BankAccount(234,22222,'Bianca',200)
print(second_BA.get_balance())

third_BA= BankAccount(345,33333,'Carmen',300)
print(third_BA.get_balance())

forth_BA= BankAccount(345,44444,'Darius',400)
print(forth_BA.get_balance())


def max_balance(*args):
    max_bal= max(arg.balance for arg in args)
    max_acc_name = list(filter(lambda arg :arg.balance == max_bal, args))[0].name
    print(f'The account holder {max_acc_name} has the highest balance : £{max_bal}')
max_balance(first_BA, second_BA, third_BA, forth_BA)

forth_BA.make_transaction(-1000)
forth_BA.make_transaction(1000)
print(forth_BA.get_balance())
print(forth_BA.get_transaction())
print(f'No of transactions: {forth_BA.num_transactions()}')
print(f'number of account {second_BA.no_accounts}')
forth_BA.__delete__()
print(f'number of account {second_BA.no_accounts}')