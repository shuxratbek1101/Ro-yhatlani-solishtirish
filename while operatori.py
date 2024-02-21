# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:52:29 2024

@author: user
"""

#savol='yaxshi korgan kitobingizni kiriting:'
#savol+='\n(dasturni to\'xtatish uchun stop deb yozing)\n>>>'
#qiymat=''
#while qiymat != 'stop':
#    qiymat=input(savol)
#    if qiymat=='stop':
#        print('dastur tugadi')
###----------------------------------------------------------------------------
#1
#savol='istalgan sonni kvadratini hisoblocvhi dastur.Istalgan son kiriting:'
#savol+='\n(to\'xtatish uchun stopni bosing)\n>>>'   
#qiymat=''
#while qiymat!='stop':
#    qiymat=input(savol)
#    if qiymat=='stop':
#        print('dastur tugadi')
#    else:
#        print(float(qiymat)**2)
###----------------------------------------------------------------------------
#2 
#Flag ishora orqali
#savol='istalgan sonni kvadratini hisoblocvhi dastur.Istalgan son kiriting:'
#savol+='\n(to\'xtatish uchun stopni bosing)\n>>>'   
#ishora=True
#while ishora:
#    qiymat=input(savol)
#    if qiymat=='stop':
#        ishora=False
#        print('dastur tugadi')
#    else:
#        print(float(qiymat)**2)       
#------------------------------------------------------------------------------
#3
#break orqali
#savol='istalgan sonni kvadratini hisoblocvhi dastur.Istalgan son kiriting:'
#savol+='\n(to\'xtatish uchun stopni bosing)\n>>>'   
#while True:
#    qiymat=input(savol)
#    if qiymat=='stop':
#      print('dastur tugadi')
#      break
#    else:
#        print(float(qiymat)**2)       
#------------------------------------------------------------------------------
#4 break
#savol='yoshingizni kiriting:'
#savol+='\n(dasturdan chiqish uchun "exit" yoki "stop" deb yozing!)\n>>>'
#while True:
#    qiymat=input(savol)
#    if qiymat=='stop' or qiymat=='exit':
#        print('dastur tugadi')
#        break
#    elif int(qiymat)<=7:
#        print('chipta narxi: 2000')
#    elif int(qiymat)>7 and int(qiymat)<18:
#        print('chipta narxi:3000')
#    elif  int(qiymat)>=18 and int(qiymat)<65:
#        print("chipta narxi:10000")
#    elif int(qiymat) >=65:
#        print('chipta bepul!')
   
#------------------------------------------------------------------------------     
#5 flag orqali        
#savol='yoshingizni kiriting:'
#savol+='\n(dasturdan chiqish uchun "exit" yoki "stop" deb yozing!)\n>>>'
#ishora=True
#while ishora:
#    qiymat=input(savol)
#    if qiymat=='stop' or qiymat=='exit':
#        ishora=False
#        print('dastur tugadi')
#    elif int(qiymat)<=7:
#        print('chipta narxi: 2000')
#    elif int(qiymat)>7 and int(qiymat)<18:
#        print('chipta narxi:3000')
#    elif  int(qiymat)>=18 and int(qiymat)<65:
#        print("chipta narxi:10000")
#    elif int(qiymat) >=65:
#        print('chipta bepul!')
  
savol='yoshingizni kiriting:'
savol+='\n(dasturdan chiqish uchun "exit" yoki "stop" deb yozing!)\n>>>'
qiymat=('')
while qiymat!='stop' or qiymat!='exit':
    qiymat=input(savol)
    if qiymat=='stop' or qiymat=='exit':
        print('dastur tugadi')
        break
    elif int(qiymat)<=7:
        print('chipta narxi: 2000')
    elif int(qiymat)>7 and int(qiymat)<18:
        print('chipta narxi:3000')
    elif  int(qiymat)>=18 and int(qiymat)<65:
        print("chipta narxi:10000")
    elif int(qiymat) >=65:
        print('chipta bepul!')  
    