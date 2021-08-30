import pandas as pd

data = {'num_habitacions':  ['3', '4', '3', '6', '4'],
        'tamany_pis': ['75', '80', '70', '120', '90'],
        'num_lavabos': ['1', '2', '1', '3', '2']
        }

df = pd.DataFrame (data)

df.head()
