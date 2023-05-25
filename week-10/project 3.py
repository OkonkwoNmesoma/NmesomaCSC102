import pandas as pd
class Niger_breweries():
    def table(self):
        Nigerian_breweries = {'LAGER' : ['33 EXPORT', 'Desperados','Goldberg', 'Gulder', 'Heineken', 'Star'],
                              'STOUT' : ['Legend', 'Turbo King', 'Williams', '', '', ''],
                              'NON-ALCOHOLIC': ['Maltina', 'Amstel Malta', 'Malta Gold', 'Fayrouz', '', '']
        }
        df = pd.DataFrame(Nigerian_breweries)

        df.to_csv('Nigerian Breweries.csv')

N = Niger_breweries()
N.table()