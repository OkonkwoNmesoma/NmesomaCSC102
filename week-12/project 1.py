from abc import ABC

class abstract(ABC):
    def fan_page(self):
        pass

class FC_Cirok(abstract):
    def fan_page(self):
        print("Welcome to FC CIROK")

class Madiba(abstract):
    def fan_page(self):
        print("Welcome to Madiba")

class Blue_Jays(abstract):
    def fan_page(self):
        print("Welcome to Blue Jays")

class TSG_Walker(abstract):
    def fan_page(self):
        print("Welcome to TSG WALKERS")
club = input("What club do you support: ")
if club == str.casefold("FC Cirok"):
    F = FC_Cirok()
    F.fan_page()
elif club == str.casefold("Madiba"):
    M = Madiba()
    M.fan_page()
elif club == str.casefold("Blue Jays"):
    B = Blue_Jays()
    B.fan_page()
elif club == str.casefold("TSG Walkers"):
    T = TSG_Walker()
    T.fan_page()
else:
    print("Invalid Input")

