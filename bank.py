class Account:
    def __init__(self):
        self.balance=0
        print('Your Account is Created.')
    def deposit(self):
        amount=int(input('Enter the amount to deposit:'))
        self.balance+=amount
        print('Your New Balance =%d' %self.balance)
    def withdraw(self):
        amount=int(input('Enter the amount to withdraw:'))
        if(amount >10000):
            #print("LimitExeedexception")
            raise LimitedExceedException(" your transaction limit is over")

        elif(amount<100):
            #print('InvalidMinimumException')
            raise InvalidMinimumException(" your transaction limit is invalid")

        
        elif(amount>self.balance):
            #print('InsufficientFundException!')
            raise InsufficientFundException("your transaction account is insufficient")

        else:
            self.balance-=amount
            print('Your Remaining Balance =%d' %self.balance)
            print('your with draw amount', amount)
    def enquiry(self):
        print('Your Balance =%d' %self.balance)
        
account= Account()
account.deposit()
account.withdraw()
account.enquiry()
