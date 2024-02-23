# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:36:50 2024

@author: user
"""

#savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:
#    qiymat = input(savol)
#    if qiymat=='exit':
#        print('dastur tugadi')
#        break
#    elif int(qiymat)<0:
#        continue
   
#    else:
#        ildiz = float(qiymat)**(0.5)
#        print(f"{qiymat} ning ildizi {ildiz} ga teng")
#-----------------------------------------------------------------------------=
#1
#print('buyurtmangizni kiriting')
#buyurtmalar=[]
#n=1
#while True:
#    buyurtma=input(f"{n}-buyurtmangizni kiriting:")
#    buyurtmalar.append(buyurtma)
#    javob = input('Yana zakas qilishni hohlaysizmi? (ha\yo\'q) ')
#    if javob.lower()=='ha' :
#        n+=1    
#    else:
#        break
#print('sizning buyurtmalaringiz:')   
#for buyurtma in buyurtmalar:
#    print(f"{buyurtma.title()}")
#-----------------------------------------------------------------------------
#2
#print('mahsulotlaringizni kiriting')
#items={}
#ishora=True
#while ishora:
#    mahsulot=input(f"Maxsulot nomini kiriting:")
#    narx=input(f"{mahsulot.title()}-narxini kiriting:")
#    items[mahsulot]=int(narx)
    
#    javob=input('Yana maxsulot kiritishni xohlaysizmi? (ha/yo\'q)')
#    if javob=='yo\'q':
#        ishora=False
 
#print('Maxsulotlaringiz:')
#for ism, narx in items.items():
#    print(f'{ism.title()}ning narxi {narx}')
#------------------------------------------------------------------------------
#3
print('mahsulotlaringizni kiriting')
ebozor={'telefon':'1_500_000','kompyuter':'7_000_000','radio':'500_000'}
items={}
ishora=True
while ishora:
    mahsulot=input(f"Maxsulot nomini kiriting:")
    narx=input(f"{mahsulot.title()}-narxini kiriting:")
    items[mahsulot]=int(narx)
    
    javob=input('Yana maxsulot kiritishni xohlaysizmi? (ha/yo\'q)')
    if javob=='yo\'q':
        ishora=False
 
print('Maxsulotlaringiz:')
for ism, narx in items.items():
    if ism in ebozor.keys():
       print(f"{ism.title()} bizda mavjud")  
    else:
        print(f'{ism.title()}ning narxi {narx}')

               
    
    
    
    