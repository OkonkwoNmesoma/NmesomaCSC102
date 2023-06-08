import pandas as pd

class students():
    data = pd.read_csv("sis.csv")
    def check(self):
        data = pd.read_csv("sis.csv")
        name = input('ENTER NAME')
        if name in data['Name'].tolist():


