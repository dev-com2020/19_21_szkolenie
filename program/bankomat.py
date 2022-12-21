class Bankomat:
    '''
    symulacja bankomatu
    '''

    def __init__(self, balance):
        self.__balance = balance

    def despoit(self, amount):
        self.__balance += amount

    def __withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Zbyt mała ilośc na koncie')

    def pin(self, amount):
        pin = int(input('Podaj pin:'))
        if pin == 1597:
            self.__withdraw(amount)
        else:
            print('Zły PIN!!!')

    def get_balance(self):
        return self.__balance
