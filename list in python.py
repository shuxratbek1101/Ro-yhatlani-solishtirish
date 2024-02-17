# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:49:30 2024

@author: user
"""

mahsulotlar=['anor','uzum','banan','nok','olma','mandarin','kivi','apelsin','gilos','shaftoli']
buyurtmalar=[]
a=int(input('nechta maxsulot olasiz? '))
for n in range(a):
    buyurtmalar.append(input(f" savatga {n+1}- maxsulotingizni kiriting: "))

bor_maxsulotlar=[]
mavjud_emas=[]
for maxsulot in buyurtmalar:
    if maxsulot in mahsulotlar:
        bor_maxsulotlar.append(maxsulot)
    else:
        mavjud_emas.append(maxsulot)
        
if mavjud_emas:
    print('bunday maxsulotlar mavjud emas')
    for maxsulot in mavjud_emas:
        print(maxsulot)
else :
    print('Siz so\'ragan barcha maxsulotlar do\'konimizda bor')