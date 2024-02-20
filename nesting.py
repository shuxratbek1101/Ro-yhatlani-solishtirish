# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:41:37 2024

@author: user
"""
#LUG'AT ICHIDA RO'YXAT

#1

#friend0={'ismi':'muxriddin','s_kino':['jumong','jangbobo','tabib']}
#friend1={'ismi':'uchqun','s_kino':['merlin','lyusi','jangbobo']}
#friend2={'ismi':'bekzod','s_kino':['kuydirgi','tezlik','shavqatsiz']}
#friends=[friend0,friend1,friend2]
#for friend in friends:
#    print(f"{friend['ismi']}ning sevimli kinosi {friend['s_kino']} ")

#------------------------------------------------------------------------------
#2

#dasturchilar = {
#    'ali':['python','c++'],
#    'vali':['html','css','js'],
#    'hasan':['php','sql'],
#    'husan':['python','php'],
#    'maryam':['c++','c#']
#    }

#for ism, tillar in dasturchilar.items():
#      print(f"{ism.title()} quyidagi dasturlash tillarini biladi:")
#      for til in tillar:
#        print(til)
#------------------------------------------------------------------------------

#LUG'AT ICHIDA LUG'AT

countries = {
    "uzbekistan":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholisi':33_000_000,
                   'pul birligi':"so'm"
                   },
    
    'rossiya':{'poytaxt':"moskva",
                'maydon':17_000_000,
               'aholisi':140_000_000,
               'pul birligi':'rubl'},
    
    'usa':{'poytaxt':"vashington",
            'maydon':963100,
            'aholisi':327000000,
            'pul birligi':'dollar'}     
    }
a=input('qaysi davlat haqida malumot olmoqchisiz?\n>>>')
a=a.lower()

if a in countries.keys() :
        v=countries[a]
      
        print(f"{a.title()} davlatini poytaxti {v['poytaxt'].title()} "
            f"\nmaydoni {v['maydon']}"
           f"\naholisi {v['aholisi']}"
           f"\npul birligi {v['pul birligi']}")
else:
    print('bizda bunday davlat yoq')
       
            
      