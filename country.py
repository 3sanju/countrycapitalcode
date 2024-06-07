class Country:
    def __init(self,country=None,capital=None):
        self.country=country
        self.capital=capital
    def add(self,num):
        lst={ }
        for _ in range(0,num):
         p=input("Enter the name of country")
         q=input("Enter the name of capital")
         lst[p]=q
        print(lst)
num=int(input("enter the number of countries"))
countries=Country()
countries.add(num)

