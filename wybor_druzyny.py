# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:03:00 2019

@author: Alicja
"""

#%%
import pandas as pd

#%%
df = pd.read_csv("https://raw.githubusercontent.com/AlicjaHol/kwaternion/master/modified.csv")


#%%
mega = df[(df.Legendary == False) & (df.Name.str.contains('Mega'))].sort_values('Total', ascending =  False)
niemega = df[(df.Legendary == False) & ~(df.Name.str.contains('Mega'))].sort_values( 'Total', ascending =  False)
#%%
#mozliwe typy pokemonow
typy = list(df.groupby('Type1').size().index)
#%%
czy_lider = input("czy jestes liderem (t/n) ")
if(czy_lider == "t"):
    
    twoj_typ = input("podaj typ ")
    twoj_typ = twoj_typ.lower().capitalize()
    if (twoj_typ in typy):
        twoj_mega = mega[mega.Type1 == twoj_typ].iloc[0].Name
        twoje_niemega = list(niemega[niemega.Type1 == twoj_typ].iloc[0:5].Name)
    else:
        raise Exception('nieprawidlowy typ. lista mozliwych typow to {}'.format(typy))
elif(czy_lider == "n"):
    twoj_mega = mega.iloc[0].Name
    twoje_niemega = list(niemega.iloc[0:5].Name)
else:
    raise Exception('nieprawidlowa odpowiedz na pytanie o lidera')
#%%    
druzyna = [twoj_mega]+ twoje_niemega
#%%
twoja_druzyna = pd.DataFrame()

for poke in druzyna:
    twoja_druzyna = pd.concat([twoja_druzyna, df[df.Name==poke]])
#%%
print("\t\t\t TWOJA DRUŻYNA \n")
print(twoja_druzyna.loc[:,['Name', 'Type1', 'Total']])