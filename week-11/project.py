import pandas as pd

class students():
    data = pd.read_csv("sis.csv")
    def check(self):
        pirates = data['Age'] > 14 and data['Age'] < 18
        yankees = data['Age'] > 18 and data['Age'] > 22
        bulls = data['Age'] > 22

        pirates.to_csv("THE PIRATES")
        yankees.to_csv("THE YANKEES")
        bulls.to_csv("THE BULLS")

ss = students()
data = pd.read_csv("sis.csv")
name = input("ENTER NAME: ")
if name in data['Name'].tolist():
    ss.check()
