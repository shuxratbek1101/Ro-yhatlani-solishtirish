# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:51:37 2024

@author: user
"""

# def oraliq(min,max,d):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += d
#     return sonlar
# print(oraliq(1, 10, 3))
#=============================================================================
# def user(ismi,familiyasi,t_yili,t_joyi,e_manzil=None,tel_raqami=None):
#     users={'ismi':ismi,
#           'familiya':familiyasi,
#           't_yili':t_yili,
#           't_joyi':t_joyi,
#           'e_manzil':e_manzil,
#           'tel_raqam':tel_raqami}
#     return users
# print(user("shuxrat", "tojimurodov", 2003, "andijon"))
#==============================================================================
## lugatli funksiya bilan royhatni toldirish
# def user(ismi,familiyasi,t_yili,t_joyi,e_manzil=None,tel_raqami=None):
#     users={'ismi':ismi,
#           'familiya':familiyasi,
#           't_yili':t_yili,
#           't_joyi':t_joyi,
#           'e_manzil':e_manzil,
#           'tel_raqam':tel_raqami}
#     return users
# print('Mijozlarimiz haqida malumotlar:')
# mijozlar=[]
# while True:
#     print("\n Quyidagi ma'lumotlarni kiriting:")
#     ism=input('\nismingizni kiriting:')
#     familiy=input("\nFamiliyangizni kiriting:")
#     t_yil=input("\n Tug'ilgan yilingizni kiriting:")
#     t_joy=input("\nTug'ilgan joyingizni kiritng:")
#     e_manzil=input("\nElektron pochta manzilingizni kiriting:")
#     tel_raqam=input("\nTelefon raqamingizni kiriting:")
#     mijozlar.append(user(ism,familiy,t_yil,t_joy,e_manzil,tel_raqam))
#     javob=input("\nYana mijoz qo'shishni istaysizmi? (ha/yo'q)")
#     if javob=="yo'q":
#         break
    
# for mijoz in mijozlar:
#     print(mijoz)
#==============================================================================
#eng katta son
# def max(a,b,c):
#     eng_max=[]
#     if a>b and a>c:
#         eng_max.append(a)
#         print(f"eng katta son {eng_max}")
#     elif b>a and b>c:
#         eng_max.append(b)
#         print(f"eng katta son {eng_max}")
#     elif c>a and c>b:
#         eng_max.append(c)
#         print(f"eng katta son {eng_max}")
#     return eng_max
# print(max(5, 8, 1))
#==============================================================================
#aylana    
# def aylana (r):
#     d=2*r
#     p=2*3.14*r
#     s=3.14*(r)**2
#     info={'diamter':d,
#           'perimetri':p,
#           'yuzi':s}
#     return info
# print(aylana(1))

# #prime numbers
# def prime_numbers(min, max):
#     tub_numbers = []
#     for n in range (min,max+1):
#         tub = True
#         if n==1:
#             tub=False
#         elif n==2:
#             tub=True
#         else:
#             for a in range(2,n):
#                 if n%a==0:
#                     tub=False
#         if tub:
#             tub_numbers.append(n)

#     return tub_numbers

# print(prime_numbers(1,15))

def fibo_numbers(n):
    sonlar=[]
    for a in range(n):
        if a==0 or a==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[a-1]+sonlar[a-2])
    return sonlar
print(fibo_numbers(11))


        
    