# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:01:58 2024

@author: user
"""
def katta_harf(matnlar):
    matnlar=matnlar[:]
    katta=[]
    while matnlar:
        ism=matnlar.pop()
        a=ism.title()
        katta.append(a)
    return katta
ismlar = ['ali', 'vali', 'hasan', 'husan']
print(katta_harf(ismlar))
print(ismlar)
# def katta_harf(matnlar):
#     katta = []
#     while matnlar:
#         ism = matnlar.pop()
#         a = ism.title()
#         katta.append(a)
#     return katta

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# print(katta_harf(ismlar))
