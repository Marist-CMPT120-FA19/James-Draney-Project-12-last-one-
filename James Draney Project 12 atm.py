#jamesdraney
#james.draney1@marist.edu
#finalproject
#letsgetthisbread
#IMPORTANT PROFESSOR GIORGI:
#WHEN PROMPTED FOR USERID WRITE james or professor AND THE FOLLOWING PIN,
#FOUND IN THE TEXT FILE ACCOUNTS

class ATM:
    users = {}
    checking_accounts = {}
    savings_accounts = {}

    def __init__(self):
        
        with open("accounts.txt", "r") as filestream:
            for line in filestream:
                account_line = line.split(",")
                self.users[account_line[0]] = int(account_line[1])
        
        with open("checking.txt", "r") as filestream:
            for line in filestream:
                checking_line = line.split(",")
                self.checking_accounts[checking_line[0]] = int(checking_line[1])
        
        with open("savings.txt", "r") as filestream:
            for line in filestream:
                savings_line = line.split(",")
                self.savings_accounts[savings_line[0]] = int(savings_line[1])

    def check_balance(self, account_type, user):
        if account_type == 'checking':
            if self.checking_accounts.get(user):
                return str(self.checking_accounts[user])
            else:
                return 'Checking account does not exist'
        elif account_type == 'savings':
            if self.savings_accounts.get(user):
                return str(self.savings_accounts[user])
            else:
                return 'Saving account does not exist'
        else:
            return 'Invalid account type'
    
    def withdraw_cash(self, account_type, user, amount):
        if account_type == 'checking':
            if self.checking_accounts.get(user):
                if amount > self.checking_accounts[user]:
                    return 'Insufficient funds'
                else:
                    self.checking_accounts[user] -= amount
                    return 'Transaction succeeded'
            else:
                return 'Checking account does not exist'
        elif account_type == 'savings':
            if self.savings_accounts.get(user):
                if amount > self.savings_accounts[user]:
                    return 'Insufficient funds'
                else:
                    self.savings_accounts[user] -= amount
                    return 'Transaction succeeded'
            else:
                return 'Saving account does not exist'
        else:
            return 'Invalid account type'

    def transfer_money(self, account_to_type, account_from_type, user, amount):
        if self.checking_accounts.get(user) == None or self.savings_accounts.get(user) == None:
            return 'Need to create both account types first'
        else:
            if account_from_type == 'checking':
                if amount > self.checking_accounts[user]:
                    return 'Insufficient funds'
                else:
                    self.checking_accounts[user] -= amount
                    self.savings_accounts[user] += amount
                    return 'Transaction succeeded'
            else:
                if amount > self.savings_accounts[user]:
                    return 'Insufficient funds'
                else:
                    self.savings_accounts[user] -= amount
                    self.checking_accounts[user] += amount
                    return 'Transaction succeeded'
    
    def save_file(self):
        checking_file = open('checking.txt', 'w')
        checking_data = []
        for user in self.checking_accounts:
            checking_data.append(user + ',' + str(self.checking_accounts[user]) + '\n')
        checking_file.writelines(checking_data)

        savings_file = open('savings.txt', 'w')
        savings_data = []
        for user in self.savings_accounts:
            savings_data.append(user + ',' + str(self.savings_accounts[user]) + '\n')
        savings_file.writelines(savings_data)
    
    def main(self):
        userID = ''
        while True:
            print('Enter userID or exit to leave:')
            userID = input()
            if userID == 'exit':
                break
            if self.users.get(userID):
                print('Enter PIN')
                pin = int(input())
                if pin == self.users[userID]:
                    print('Sucessfully logged in!')
                    break
                else:
                    print('Wrong, please retry!')
        option = ''
        while option != '0' and userID != 'exit':
            print('0 to exit')
            print('1 to check balance')
            print('2 to withdraw cash')
            print('3 to transfer money')
            print('Enter an option:')
            option = input()
            if option == '1':
                print('Enter account type (checking or savings)')
                account_type = input()
                print(self.check_balance(account_type, userID))
            if option == '2':
                print('Enter account type (checking or savings)')
                account_type = input()
                print('Enter amount')
                amount = int(input())
                print(self.withdraw_cash(account_type, userID, amount))
            if option == '3':
                print('Enter account from type (checking or savings)')
                account_from_type = input()
                print('Enter account to type (checking or savings)')
                account_to_type = input()
                print('Enter amount')
                amount = int(input())
                print(self.transfer_money(account_to_type, account_from_type, userID, amount))
        self.save_file()
        print('GOODBYE')


atm = ATM()
atm.main()
 
