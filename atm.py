class ATM():
    def __init__(self,card_number,pin_number,total_money):
        self.card_number = card_number
        self.pin_number= pin_number
        self.total_money= total_money
    
    def CashWithdrawl(self):
        withdraw=int(input('How much money you want to withdraw'))
        print('You have withdrawn $'+withdraw)
        currrentmoney=self.total_money-withdraw
        print('Your balance left is $'+ currrentmoney)

    def BalanceEnquiry(self):
        print('Your balance is $'+ self.total_money)


atm = ATM('9225200707','9850397826','500')
atm.CashWithdrawl()
atm.BalanceEnquiry()
