import pandas as pd
from abc import ABC

class abstract(ABC):
    def external_vendors(self):
        pass
class coop(abstract):
    def external_vendors(self):
        data = {"Main Meal": ["Jollof Rice and Stew", "White Rice and Stew", "Fried Rice", "Salad", "Plantain"],
                "Price": [200, 200, 200, 100, 100]}
        df = pd.DataFrame(data)
        df.to_csv('coop.csv')
        print(df)
class Faith(abstract):
    def external_vendors(self):
        data = {"Main Meal": ["Fried Rice", "White Rice and Stew", "Jollof Rice", "Beans", "Chicken"],
                "Price": [400, 400, 400, 200, 800]}
        df = pd.DataFrame(data)
        df.to_csv('Faith.csv')
        print(df)
class stud(abstract):
    def external_vendors(self):
        data = {"Main Meal": ["Chicken Fried Rice", "Pomo Sauce", "Spaghetti Jollof", "Amala/Ewedu", "semo with Eforiro soup"],
                "Price": [800, 300, 500, 500, 500]}
        df = pd.DataFrame(data)
        df.to_csv('stud.csv')
        print(df)

vendor = input("Where do you want to get food from?: ")
if vendor == str.casefold("coop"):
    C = coop()
    C.external_vendors()
elif vendor == str.casefold("Faith"):
    F = Faith()
    F.external_vendors()
elif vendor == str.casefold("Student"):
    S = stud()
    S.external_vendors()
else:
    print("Invalid Input")