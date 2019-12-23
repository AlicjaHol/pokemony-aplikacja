# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:01:30 2019

@author: Alicja
"""

#%%
import pandas as pd
import tkinter as tk
#%%
def lider():
    ramka_lidera.destroy()
    ramka_typu = tk.Frame(okno, bg = 'white', bd = 5)
    ramka_typu.place(relx = 0, rely =0, relwidth = 1, relheight = 1)
    wybrany_typ= tk.StringVar()
    wybrany_typ.set(None)
    przyciski_typow = []
    for i in range(licz_typow):
        przyciski_typow.append(tk.Radiobutton(ramka_typu, text = typy[i], value = typy[i], variable = wybrany_typ))
    przyciski_typow.append(tk.Button(ramka_typu, text = "Wybierz typ", command = lambda:wytypowany(wybrany_typ, ramka_typu)))
    for (i, btn) in enumerate(przyciski_typow):
        btn.pack(fill = tk.BOTH, expand = tk.YES)
#%%
def wytypowany(wybrany_typ, ramka_typu):
    ramka_typu.destroy()
    wybrany_typ = wybrany_typ.get()


    
    


    ramka_mega = tk.Frame(okno, bd = 5)
    ramka_mega.place(relx =0, rely =0, relwidth =1, relheight =1)
    etykietka = tk.Label(ramka_mega, text = 'Proponowane mega ewolucje', bg= 'yellow')
    etykietka.pack(expand = 'yes')
    twoje_mega = mega[mega.Type1 == wybrany_typ].iloc[0:3]
    twoje_mega = twoje_mega.loc[:, ['Name', 'Type1', 'Type2', 'Total']]
    druzyna =tk.Label(ramka_mega, text = twoje_mega)
    druzyna.pack(expand ='yes', fill = 'both')
    etykietka2 = tk.Label(ramka_mega, text = 'Proponowane zwykłe pokemony', bg ='yellow')
    etykietka2.pack(expand = 'yes')
    twoje_niemega = niemega[niemega.Type1 == wybrany_typ].iloc[0:10]
    twoje_niemega = twoje_niemega.loc[:, ['Name', 'Type1', 'Type2', 'Total']]
    druzyna2 = tk.Label(ramka_mega, text = twoje_niemega)
    druzyna2.pack(expand = 'yes', fill = 'both')
    


#%%
def nielider():
    ramka_lidera.destroy()
    twoje_mega = mega.iloc[0:3]
    twoje_mega = twoje_mega.loc[:, ['Name', 'Type1', 'Type2', 'Total']]
    twoje_niemega = niemega.iloc[0:10]
    twoje_niemega = twoje_niemega.loc[:, ['Name', 'Type1', 'Type2', 'Total']]
    ramka_mega = tk.Frame(okno, bd = 5)
    ramka_mega.place(relx =0, rely =0, relwidth = 1, relheight =1)
    etykietka = tk.Label(ramka_mega, text = 'Proponowane mega ewolucje', bg = 'yellow')
    etykietka.pack(expand = 'yes')
    druzyna =tk.Label(ramka_mega, text = twoje_mega)
    druzyna.pack(expand ='yes', fill = 'both')
    etykietka2 = tk.Label(ramka_mega, text = 'Proponowane zwykłe pokemony', bg = 'yellow')
    etykietka2.pack(expand = 'yes')
    druzyna2 = tk.Label(ramka_mega, text = twoje_niemega)
    druzyna2.pack(expand = 'yes', fill = 'both')
    
    
    
#%%    
HEIGHT = 600
WIDTH = 400
#%%
okno = tk.Tk()
okno.title("Wybierz swoją drużynę Pokemon!")
canvas = tk.Canvas(okno, height = HEIGHT, width = WIDTH)
canvas.pack()


ramka_lidera = tk.Frame(okno, bd = 5, bg = 'white')
ramka_lidera.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
etykieta = tk.Label(ramka_lidera, text = "Czy jesteś liderem pokemon?", bg = 'yellow')
etykieta.pack(expand = True, fill = 'both')
tak = tk.Button(ramka_lidera, text = 'Tak', command = lider)
tak.pack(expand = True, fill = 'both')
nie = tk.Button(ramka_lidera, text = 'Nie', command = nielider)
nie.pack(expand = True, fill = 'both')
#%%
df = pd.read_csv("https://raw.githubusercontent.com/AlicjaHol/kwaternion/master/modified.csv")
#%%
mega = df[(df.Legendary == False) & (df.Name.str.contains('Mega'))].sort_values('Total', ascending =  False)
niemega = df[(df.Legendary == False) & ~(df.Name.str.contains('Mega'))].sort_values( 'Total', ascending =  False)
#%%
typy = list(df.groupby('Type1').size().index)
licz_typow = len(typy)




okno.mainloop()