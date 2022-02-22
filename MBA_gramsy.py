from pydoc import describe
import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt 
from mlxtend.frequent_patterns import apriori

data = pd.read_csv('paragony.csv', encoding="UTF-8", sep=";").drop(columns=['DataWyst','NazwaTow'])

#print(data.info())

#data['DataWyst'] = pd.to_datetime(data['DataWyst'])

#print(data.info())
#print("""This Dataset start from {} 
#                     to {}""".format(data['DataWyst'].describe()['first'],
#                                     data['DataWyst'].describe()['last']))

#top_10_transaction = pd.DataFrame(data.groupby(['ParagonNO','Symbol']).nunique().sort_values(['ParagonNO','Symbol'], ascending=False).head(10))

#print(type(top_10_transaction))
#print(top_10_transaction)

#

#
#print(data)
basket_plus = data.groupby(['ParagonNO','Symbol'])['lp'].sum().unstack().reset_index().fillna(0).set_index('ParagonNO')
#print(type(basket_plus))
#

#print(basket_plus)

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
    
basket_encode_plus = basket_plus.applymap(encode_units)
#basket_encode_plus


frequent_itemsets_plus = apriori(basket_encode_plus, min_support=0.0025, 
                                  use_colnames=True).sort_values('support', ascending=False).reset_index(drop=True)
#

#
frequent_itemsets_plus['length'] = frequent_itemsets_plus['itemsets'].apply(lambda x: len(x))
#
print("czeste produkty")
print(frequent_itemsets_plus)
from mlxtend.frequent_patterns import association_rules
print(association_rules(frequent_itemsets_plus, metric='lift', 
                  min_threshold=1).sort_values('lift', ascending=False).reset_index(drop=True))