# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 22:45:10 2024

@author: user
"""

#python={'boolean':'mantiqiy qiymat','float':'onlik son','for':'biror amalni qayta qayta bajarish sikli','if':'shartlarni tekshirish sikli','integer':'butub son'}
#print('python terminlari:')
#for k,q in python.items():
#    print(f"{k.title()}-{q}")
#----------------------------------------------------------
#countries={'uzbekistan':'tashkent','usa':'vashington','england':'london','germany':'berlin','japan':'tokio','china':'pekin'}
#print('Davlatlar: Poytaxtlar:')
#for k,q in sorted(countries.items()) :
#    print(f"{k.title()}-{q.title()}")
#-----------------------------------------------------------
#countries={'uzbekistan':'tashkent','usa':'vashington','england':'london','germany':'berlin','japan':'tokio','china':'pekin'}
#country=input('Qaysi davlat poytaxtini bilishni xohlaysiz?\n>>>').lower()
#for a in countries:
#    if a==country:
#        print(f"{a.title()}ning poytaxti {countries[a]}")
#------------------------------------------------------------
meals={'osh':'25000','bishteks':'23000','shashlik':'15000','kabob':'20000','gril':'30000'}
buyurtma=[]
k=int(input('Necchta taom olasiz?\n>>>'))
for n in range(k):
    buyurtma.append(input(f"{n+1}-taomingizni kiriting:\n>>>").lower())

for a in buyurtma:
    if a in meals:
        print(f"{a.title()} taomining narxi {meals[a]}")
    else:
        print(f"bizda {a.title()} taomi yo'q")