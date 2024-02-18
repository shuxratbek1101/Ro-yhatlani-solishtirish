# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:38:52 2024

@author: user
"""

python={'integer':'butun sonlar uchun','float':'onlik qiymat uchun','string':'matn uchun','list':'royhat','tuple':'ozgarmas royhat','dictionary':'lugat','function':'funksiya'}
kalit=input('kalit soz kiriting: ').lower()
tarjima=python.get(kalit)
if tarjima==None:
    print('bunday so\'z mavjud emas')
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
        
        