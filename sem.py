"""
Sual 1. Məhsul Alış-Verişi
a. İstifadəçidən bir elektronika mağazasından aldığı 6 məhsulun adını və qiymətini alın.
b. Məhsulları qiymətlərinə görə artan sırada sıralayın və çap edin.
c. Ümumi xərcləri hesablayın və əgər bu xərc 300 manatdan azdırsa,
10% endirim tətbiq edin və nəticəni ekrana çap edin
"""
siyahi={}
for i in range(0, 6):
    mehsul=input('mehsulun adini daxil edin:')
    qiymet=int(input("mehsulu  qiymetini daxil edin:"))
    siyahi[mehsul]=qiymet
    artansiyahi = dict(sorted(siyahi.items(), key=lambda x: x[1]))
print(artansiyahi)
umumi = sum(siyahi.values())
if umumi < 300:
    umumi = umumi * 0.9
else:
    umumi= umumi
print(umumi)