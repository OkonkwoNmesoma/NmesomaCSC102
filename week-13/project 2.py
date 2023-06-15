import pandas as pd

COMPANY = {'COMPANY':['ENRON COOPERATION','ANDERSON COOPERATION','GK JONES','MICA INDUSTRIES','DUNE INDUSTRIES'],
           'DATE FOUNDED':[1987,1936,2001,1996,2008],
           'COMPANY SHARES':[1000000,1500000,3000000,250000,800000],
           'COMPANYS LIABILITY': [200000,500000,1500000,50000,300000],
           'PERCENTAGE LEVERAGE':['80%','66.67%','50%','80%','62.5%']}

df = pd.DataFrame(COMPANY)
print(df)
df.to_csv('COMPANY.csv')