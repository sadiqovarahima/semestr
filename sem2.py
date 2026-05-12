"""
Sual 2. Supermarket Alış-Verişi
a. İstifadəçidən supermarketdən aldığı 7 məhsulun adını və qiymətini alın.
b. Məhsulları qiymətlərinə görə azalan sırada sıralayın və çap edin.
c. Ümumi xərcləri hesablayın və əgər bu xərc 150 manatdan çoxdursa,
 8% endirim tətbiq edin və nəticəni ekrana çap edin.
"""
siyahi={}
for i in range(0, 7):
    mehsul=input('mehsulun adi')
    qiymet=int(input('mehsulun qiymeti'))
    siyahi[mehsul]=qiymet
    azalansiyahi = dict(sorted(siyahi.items(), key=lambda x: x[1]))
print(azalansiyahi)
umumi = sum(siyahi.values())
if umumi > 150:
    umumi = umumi * 0.92
else:
    umumi=umumi
print(umumi)
