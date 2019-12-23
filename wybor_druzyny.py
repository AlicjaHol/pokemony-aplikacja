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
        twoje_mega = mega[mega.Type1 == twoj_typ].iloc[0:3]
        twoje_niemega = niemega[niemega.Type1 == twoj_typ].iloc[0:10]
    else:
        raise Exception('nieprawidlowy typ. lista mozliwych typow to {}'.format(typy))
elif(czy_lider == "n"):
    twoje_mega = mega.iloc[0:3]
    twoje_niemega = niemega.iloc[0:10]
else:
    raise Exception('nieprawidlowa odpowiedz na pytanie o lidera')
    

#%%
print("\t\t Proponowane dla Ciebie mega ewolucje \n\n")
print(twoje_mega.loc[:, ['Name', 'Type1', 'Type2', 'Total']])  
#%%
print('\t\t Proponowane dla Ciebie pokemony')
print(twoje_niemega.loc[:, ['Name', 'Type1', 'Type2', 'Total']])  
#%%    
#druzyna = twoje_mega+ twoje_niemega
#%%
#twoja_druzyna = pd.DataFrame()

#for poke in druzyna:
 #   twoja_druzyna = pd.concat([twoja_druzyna, df[df.Name==poke]])
#%%
#print("\t\t\t TWOJA DRUŻYNA \n")
#print(twoja_druzyna.loc[:,['Name', 'Type1', 'Total']])