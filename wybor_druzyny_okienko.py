# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:04:46 2019

@author: Alicja
"""
#COS NIE DZIALA Z WYSWIETLANIEM !!!!!
#%%
import tkinter as tk
#%%
import pandas as pd

#%%
df = pd.read_csv("https://raw.githubusercontent.com/AlicjaHol/kwaternion/master/modified.csv")


#%%
mega = df[(df.Legendary == False) & (df.Name.str.contains('Mega'))].sort_values('Total', ascending =  False)
niemega = df[(df.Legendary == False) & ~(df.Name.str.contains('Mega'))].sort_values( 'Total', ascending =  False)
#%%
typy = list(df.groupby('Type1').size().index)
licz_typow = len(typy)
#%%
def lider():
    okno_lidera.destroy()
    global okno_typu
    okno_typu = tk.Tk()
    okno_typu.title("Wybierz swój typ, liderze!")
    okno_typu.geometry("400x600")
    global wybrany_typ 
    wybrany_typ= tk.StringVar()
    wybrany_typ.set(None)
    przyciski_typow = []
    for i in range(licz_typow):
        przyciski_typow.append(tk.Radiobutton(okno_typu, text = typy[i], value = typy[i], variable = wybrany_typ))
    przyciski_typow.append(tk.Button(okno_typu, text = "Wybierz typ", command = wytypowany))
    for (i, btn) in enumerate(przyciski_typow):
        btn.pack(fill = tk.BOTH, expand = tk.YES)
    
    
    okno_typu.mainloop()
        
    
#%%
def wytypowany():
    okno_typu.destroy()
    twoj_typ = wybrany_typ.get()
    print("wybrałeś typ " + twoj_typ)
    twoj_typ = twoj_typ.lower().capitalize()
    if (twoj_typ in typy):
        twoj_mega = mega[mega.Type1 == twoj_typ].iloc[0].Name
        twoje_niemega = list(niemega[niemega.Type1 == twoj_typ].iloc[0:5].Name)
    else:
        raise Exception('nieprawidlowy typ. lista mozliwych typow to {}'.format(typy))
     
    druzyna = [twoj_mega]+ twoje_niemega

    twoja_druzyna = pd.DataFrame()

    for poke in druzyna:
        twoja_druzyna = pd.concat([twoja_druzyna, df[df.Name==poke]])

    wyswietl_druzyne(twoja_druzyna)
#%%
def nielider():
    okno_lidera.destroy()
    twoj_mega = mega.iloc[0].Name
    twoje_niemega = list(niemega.iloc[0:5].Name)
    druzyna = [twoj_mega]+ twoje_niemega

    twoja_druzyna = pd.DataFrame()

    for poke in druzyna:
        twoja_druzyna = pd.concat([twoja_druzyna, df[df.Name==poke]])
    wyswietl_druzyne(twoja_druzyna)
    

#%%
def wyswietl_druzyne(twoja_druzyna):
#COS NIE DZIALA Z WYSWIETLANIEM!!!!
#    type1 = []
#    for nazwa in twoja_druzyna:
#        type1.append(df[df.Name == nazwa].loc['Type1'])
#    total = []
#    for nazwa in twoja_druzyna:
#        total.append(df[df.Name == nazwa].loc['Total'])
    okno_druzyny = tk.Tk()
    okno_druzyny.title("Podziwiaj swoją drużynę")
    okno_druzyny.geometry("400x400")
    etykieta = tk.Label(okno_druzyny, text = "TWOJA DRUŻYNA:")
    etykieta.pack(fill = tk.BOTH)
    print(twoja_druzyna.loc['Name', 'Type1', 'Total'])
    okno_druzyny.mainloop()
#    print(twoja_druzyna.loc[:,['Name', 'Type1', 'Total']])
    
#    print(type1)
#    print(total)
#%%
okno_lidera = tk.Tk() #tworzymy okno graficzne

#%%
okno_lidera.title("Czy jesteś liderem?")
okno_lidera.geometry("300x350")


#%%
przyciski = []
przyciski.append(tk.Button(okno_lidera, text = "Tak", command = lider))
przyciski.append(tk.Button(okno_lidera, text = "Nie", command = nielider))
for i in przyciski:
    i.pack(fill = tk.BOTH, expand = tk.YES)
okno_lidera.mainloop()

