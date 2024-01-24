#03. Mantıksal İşlemler

#Girilen sayının pozitif ya da negatif olduğunu ekrana yazınız?

sayi=int(input("bir sayi giriniz"))
if sayi>0:
    print(sayi,"pozitif")
else:
    print(sayi,"negatif")

#Girilen tamsayının sıfır, pozitif ya da negatif olup olmadığını bulan program?

sayi=int(input("bir sayi giriniz"))
if sayi>0:
    print(sayi,"pozitif")
elif sayi==0:
    print("sayı 0")
else:
    print(sayi,"negatif")

#Vize ve Final notu girilen öğrencinin geçip geçmediğini hesaplayan program (vizenin %40,finalin %60’ı hesaplanır. Final en az 60 olmak zorundadır)

vize=int(input("vize notunuzu giriniz"))
final=int(input("final notunuzu giriniz"))

if ((vize/100*40)+(final/100*60))>=50 and final>=60:
    print("geçtiniz,ortalama="+str((vize/100*40)+(final/100*60)))
else:
    print("kaldınız")

#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program? 

sayi_1=int(input("ilk sayıyı giriniz"))
sayi_2=int(input("ikinci sayıyı giriniz"))
sayi_3=int(input("üçüncü sayıyı giriniz"))

if sayi_1>sayi_2 and sayi_1>sayi_3:
    print("en büyük sayı",sayi_1)
elif sayi_2>sayi_1 and sayi_2>sayi_3:
    print("en büyük sayı",sayi_2)
else:
    print("en büyük sayı",sayi_3)

#Girilen sayının 6'nın katı olduğunu bulan program?

sayi=int(input("bir sayı giriniz"))
if sayi%6==0:
    print(sayi,"6'nın tam katı")
else:
    print(sayi,"6'nın tam katı değil")

#Yüzlük notu harf notuna çeviriniz?

ogrnot=int(input("notunuzu giriniz"))
if ogrnot>=90:
    print("harf notunuz AA")
elif ogrnot>=85:
    print("harf notunuz BA")
elif ogrnot>=80:
    print("harf notunuz BB")
elif ogrnot>=75:
    print("harf notunuz CB")
elif ogrnot>=70:
    print("harf notunuz CC")
elif ogrnot>=65:
    print("harf notunuz DC")
elif ogrnot>=60:
    print("harf notunuz DD")
elif ogrnot>=50:
    print("harf notunuz FD")
else:
    print("harf notunuz FF")

#İşçi maaşı ve çocuk sayısı verilmektedir. Çocuk sayısı bir ise %5, iki ise %10, üç veya daha fazla ise %15 zam yaparak yeni maaşı hesaplayınız?

maas=int(input("maaşınızı giriniz"))
cocuk=int(input("çocuk sayısını giriniz"))

if cocuk>=3:
    print("maaşınız",maas/100*115)
elif cocuk==2:
    print("maaşınız",maas/100*110)
elif cocuk==1:
    print("maaşınız",maas/100*105)
elif cocuk==0:
    print("maaşınız",maas)
else:
    print("yanlış giriş yaptınız")

#Ekrana 1:Toplama, 2:Çıkarma,..yaz. Sonra kullanıcıdan iki sayı alıp işlemi seçerek sonucu ekranda yazan program?

islem=int(input("yapmak istediğiniz işlemi seçin\n1=toplama\n2=çıkarma\n3=çarpma\n4=bölme\n"))
sayi_1=int(input("ilk sayıyı giriniz"))
sayi_2=int(input("ikinci sayıyı giriniz"))

if islem==1:
    print("sayıların toplamı",sayi_1+sayi_2)
elif islem==2:
    print("sayıların farkı",sayi_1-sayi_2)
elif islem==3:
    print("sayıların çarpımı",sayi_1*sayi_2)
elif islem==4:
    print("sayılarınbölümü",sayi_1/sayi_2)
else:
    print("yanlış giriş yaptınız")

# Çizgi daireyi kesiyor mu, yoksa teğet mi sonucunu bulan program? 
#Çizgi: ax+by+c=0 
#Daire: (dx,dy,r) 


#A(x1,y2), B(x2,y2), C(x3,y3) üçgene ait üç nokta olduğuna göre P(xp,yp) üçgenin içinde mi dışında mı bulan program?

x_1=int(input("x-1 degerini gir"))
y_1=int(input("y-1 degerini gir"))
x_2=int(input("x-2 degerini gir"))
y_2=int(input("y-2 degerini gir"))
x_3=int(input("x-3 degerini gir"))
y_3=int(input("y-3 degerini gir"))

x_min=x_1
x_max=x_1
y_min=y_1
y_max=y_1

if x_2<x_min:
    x_min=x_2
if x_3<x_min:
    x_min=x_3

if x_2>x_max:
    x_max=x_2
if x_3>x_max:
    x_max=x_3 

if y_2<y_min:
    y_min=y_2
if y_3<y_min:
    y_min=y_3

if y_2>y_max:
    y_max=y_2
if y_3>y_max:
    y_max=y_3

x_p=int(input("x-p degerini gir"))
y_p=int(input("y-p degerini gir"))

kontrol=0
if x_min<x_p and x_p<x_max:
    kontrol+=1
if y_min<y_p and y_p<y_max:
    kontrol+=1

if kontrol==2:
    print("içinde")
else:
    print("değil")

#A, B ve C değerlerinin 0-1 aralığında olduğunu bulan prog?

sayi_1=float(input("ilk sayıyı giriniz"))
sayi_2=float(input("ikinci sayıyı giriniz"))
sayi_3=float(input("üçüncü sayıyı giriniz"))

if sayi_1>0 and sayi_1<1:
    print(sayi_1,"0-1 arasında")
elif sayi_2>0 and sayi_2<1:
    print(sayi_2,"0-1 arasında")
elif sayi_3>0 and sayi_3<1:
    print(sayi_3,"0-1 arasında")
else:
    print("sayılar 0-1 arasında değil")


#03.Lab

#1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.

for i in range(3,101,3):
    print(i)

#Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.

sayi=int(input("sayi giriniz"))
cift_top=0
tek_top=0

for i in range(sayi):
    if i%2==0:
        cift_top+=i
    else:
        tek_top+=i

print("teklerin toplamı="+str(tek_top),"çiftlerin toplamı="+str(cift_top))

#20'ye kadar olan sayıları, 10'dan küçük ve 10'dan büyük şeklinde listeleyecek Python kodu nasıl olmalıdır?

kucuk=[]
buyuk=[]

for i in range(20):
    if i<10:
        kucuk.append(i)
    elif i>10:
        buyuk.append(i)

print("10'dan kucukler:\n",kucuk,"\n10'dan buyukler\n",buyuk)

#Kullanıcının girdiği parolada Türkçe karakterlerin olmaması gerekmektedir. Buna göre kullanıcının girdiği parolada Türkçe karakter varsa 
#“Parolada Türkçe karakter kullanılamaz.” Türkçe karakter yoksa “Parolanız oluşturulmuştur.” ekrana yazdırınız.

turkce_karakter="ÜüşŞĞğçÇöÖİı"
sifre=input("bir şifre giriniz")
kontrol=0

for i in sifre:
    if i in turkce_karakter:
        kontrol=1
if kontrol==1:
    print("parolada türkçe karakter olamaz")
else:
    print("parolanız oluşturulmuştur")

#Bir while döngüsü kullanarak kullanıcının tahmin etmesi için rastgele bir sayı oyunu oluşturan programı kodlayınız.

import random
hedef=random.randint(1,10)
kontrol=0

while kontrol==0:
    sayi=int(input("sayı gir"))
    if sayi<hedef:
        print(sayi,"hedeften kucuk")
    if sayi>hedef:
        print(sayi,"hedeften buyuk")
    if sayi==hedef:
        print("tahmin dogru,sayı="+str(hedef))
        kontrol=1

#Kullanıcıdan alınan 5 sayı içerisinden for döngüsü kullanarak en küçük sayıyı bulan programı kodlayınız.

liste=[]
for i in range(5):
    sayi=int(input("sayi giriniz"))
    liste.append(sayi)
print(min(liste))

#Bir for döngüsü kullanarak Fibonacci dizisinin ilk 20 terimini hesaplayan bir Python programı nasıl yazılır?

a=1
b=1
print(a)
print(b)
t=0
for i in range(18):
    t=a+b
    a=b 
    b=t 
    print(b)

#1 den 10′ a kadar sayıları tersten yani 10′ dan geriye yazdırın.

for i in range(10,0,-1):
    print(i)
