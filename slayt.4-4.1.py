#04. Döngüsel İşlemler

#Aşağıdaki çıktıyı veren programı yazınız?

print("element       value")
for i in range(10):
    print(i,"            ",2*i+2)

#Girilen 5 sayının ortalamasını bulan program?

toplam=0
for i in range(5):
    sayi=int(input("sayi giriniz"))
    toplam+=sayi
print("girilen sayıların ortalaması",toplam/5)

#Girilen 5 sayı içerisindeki minimum ve maksimum değerleri bulan program?

liste=[]
for i in range(5):
    sayi=int(input("sayi giriniz"))
    liste.append(sayi)

en_kucuk=liste[0]
en_buyuk=liste[0]

for i in liste:
    if i<en_kucuk:
        en_kucuk=i 
    if i>en_buyuk:
        en_buyuk=i 

print("en büyük değer",en_buyuk,"en kucuk değer",en_kucuk)

#N’e kadar tek sayıları yazdıran program?

n=int(input("n değerini giriniz"))
tek_sayilar=[]

for i in range(1,n+1,2):
    tek_sayilar.append(i)

print(tek_sayilar)

#Girilen sayının tam bölenlerini bulan program?

sayi=int(input("bir sayi giriniz"))
tam_bolenler=[]

for i in range(1,sayi+1):
    if sayi%i==0:
        tam_bolenler.append(i)

print(tam_bolenler)

#a üzeri b'yi açık hesaplayan program?

taban=int(input("tabanı giriniz"))
us=int(input("üssü giriniz"))
carpim=1

if us==0:
    print(1)
else:
    for i in range(us):
        carpim*=taban
    print(carpim)

#n’e kadar ki tek sayıların toplamı, çift sayıların çarpımını hesaplayan program?

toplam=0
carpim=1
n=int(input("sayı giriniz"))

for i in range(1,n+1):
    if i%2==0:
        carpim*=i 
    else:
        toplam+=i 

print("teklerin toplamı",toplam,"çiftlerin çarpımı",carpim)

#Girilen sayının faktöriyelini hesaplayan program?

carpim=1
sayi=int(input("sayi giriniz"))

for i in range(1,sayi+1):
    carpim*=i

print(carpim)

#Girilen n değerine göre Fibonacci serisinin ( 0 1 1 2 3 5 8 … ) ilk n terimini hesaplayınız?

n=int(input("sayı giriniz"))
a=0
b=1
c=0
print("0 1",end=" ")

for i in range(n-2):
    c=a+b 
    a=b 
    b=c 
    print(c,end=" ")

#Girilen n adet sayı içerisinden pozitif, negatif ve sıfır sayısının kaçar adet tekrarlandığını bulan program?

pozitif=0
negatif=0
sifir=0
n=int(input("sayı giriniz"))

for i in range(n):
    sayi=int(input("sayı giriniz"))
    if sayi<0:
        negatif+=1
    elif sayi==0:
        sifir+=1
    else:
        pozitif+=1

print("negatif sayısı:"+str(negatif),"pozitif sayısı:"+str(pozitif),"sıfır sayısı:"+str(sifir))

#Serinin ilk elemanı, toplam eleman sayısını ve artış değeri girildiğinde seri toplam sonucunu hesaplayan program?

ilk_eleman=int(input("ilk elemanı girin"))
toplam_eleman=int(input("toplam elemanı girin"))
artis=int(input("artış miktarını girin"))
toplam=ilk_eleman

for i in range(toplam_eleman-1):
    ilk_eleman+=artis
    toplam+=ilk_eleman

print(toplam)

#fonksiyonunun x eksenini kestiği nokta sayısını bulunuz?

print("ax2+bx+c")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
delta=b**2-4*a*c

if delta>0:
    print("2 noktada keser")

elif delta==0:
    print("1 noktada keser")

else:
    print("kesmez") 

#Girilen bir sayının asal olup olmadığını bulunuz?

sayi=int(input("sayı giriniz"))
kontrol=0

for i in range(2,sayi):
    if sayi%i==0:
        kontrol=1
if kontrol==1:
    print("sayı asal değil")
else:
    print("sayı asal")

#Girilen bir sayının asal çarpanlarını bulan program?

sayi=int(input("bir sayı giriniz"))
carpanlar=[]
degisken=2

while sayi>1:
    if sayi%degisken==0:
        carpanlar.append(degisken)
        sayi/=degisken
        continue
    else:
        degisken+=1

print(carpanlar)

#Girilen sayının basamak değerleri çarpımını bulunuz?

sayi=int(input("bir sayı girin"))
carpim=1

for i in range(len(str(sayi))):
    carpim*=sayi%10
    sayi=sayi//10
    
print(carpim)

#Girilen sayının basamak değerlerinde k rakamı olmayanları listeleyen program?

sayi=int(input("bir sayı giriniz"))
k=int(input("k değerini giriniz"))

liste=[]
for i in range(len(str(sayi))):
    if sayi%10!=k:
        liste.append(10**i)
    sayi=sayi//10
print(liste)

#Girilen sayının basamak sayısını ekrana yazdıran program?

sayi=int(input("bir sayı girin"))
print(len(str(sayi)))

#TC kimlik noyu doğru girmeye zorlayınız? (11 karakter ve tamamı sayı)

#Girilen cümleyi tersten yazdırın? 

cumle=input("bir cumle girin")
yeni_cumle=""

for i in range(len(cumle)-1,-1,-1):
    yeni_cumle+=cumle[i]

print(yeni_cumle)

#Girilen cümledeki sesli ve sessiz harf sayısını bulun?

sesli_harf="AaEeUuÜüİiÖöOoIı"
sessiz_harf="QqWwRrTtYyIıPPĞğSsDdFfGgHhJjKkLlŞşZzXxCcVvBbNnMmÇç"
cumle=input("cumle gir")
sessiz_sayisi=0
sesli_sayisi=0

for i in cumle:
    if i in sesli_harf:
        sesli_sayisi+=1
    if i in sessiz_harf:
        sessiz_sayisi+=1

print("sesli harf sayısı="+str(sesli_sayisi),"sessiz harf sayısı="+str(sessiz_sayisi))

#Girilen cümlede hangi harfin kaç defa tekrarlandığını bulan prog?

cumle=input("cumle gir")
sozluk={}

for i in cumle:
    degisken=0
    for j in cumle:
        if i==j:
            degisken+=1
            sozluk[i]=degisken

print(sozluk)

#Girilen cümledeki harflerin adetlerini ekrana yazın?

cumle=input("cumle gir")
sozluk={}

for i in cumle:
    degisken=0
    for j in cumle:
        if i==j:
            degisken+=1
            sozluk[i]=degisken

print(sozluk)

#Girilen cümledeki harf adedini bulunuz?

harf_disi=".:;,-_*?/+%&^'! 1234567890"
cumle=input("cumleyı girin")
harf_sayisi=0
for i in cumle:
    if i not in harf_disi:
        harf_sayisi+=1

print(harf_sayisi)

#Girilen iki sayının OKEK (ortak katların en küçüğü) hesaplayan program?

sayi_1=int(input("ilk sayıyı girin"))
sayi_2=int(input("ikinci sayıyı girin"))
bolenler=[]

degisken=2
while sayi_1>1 or sayi_2>1:
    if sayi_1%degisken==0 and sayi_2%degisken==0:
        bolenler.append(degisken)
        sayi_1=sayi_1/degisken
        sayi_2=sayi_2/degisken
    elif sayi_1%degisken==0:
        bolenler.append(degisken)
        sayi_1=sayi_1/degisken
    elif sayi_2%degisken==0:
        bolenler.append(degisken)
        sayi_2=sayi_2/degisken
    else:
        degisken+=1

carpim=1
for i in bolenler:
    carpim*=i
print(carpim)

#Girilen iki sayının OBEB (ortak bölenlerin en büyüğü) hesaplayan program?

sayi_1=int(input("ilk sayıyı girin"))
sayi_2=int(input("ikinci sayıyı girin"))
bolenler=[]

degisken=2
while sayi_1>=degisken and sayi_2>=degisken:
    if sayi_1%degisken==0 and sayi_2%degisken==0:
        bolenler.append(degisken)
        sayi_1=sayi_1/degisken
        sayi_2=sayi_2/degisken
    else:
        degisken+=1

carpim=1
for i in bolenler:
    carpim*=i
print(carpim)

#Sayı tahmin oyunu

import random
hedef=random.randint(1,10)
kontrol=0

while kontrol==0:
    sayi=int(input("bir sayı gir"))
    if sayi>hedef:
        print("tahminin sayıdan buyuk")
    if sayi<hedef:
        print("tahminin sayıdan kucuk")
    if sayi==hedef:
        print("sayıyı buldun",hedef)
        kontrol=1

#Harf tahmin oyunu

import random
harfler="qwertyuıopğüasdfghjklşizxcvbnmöç"
hedef=random.choice(harfler)
kontrol=0
print("tahminin ettiginiz harfi kucuk bir sekilde girin")
while kontrol==0:
    tahmin=input("tahmin=")
    if tahmin==hedef:
        print("harfi buldun",hedef)
        kontrol=1

#Bir top X metre yükseklikten bırakılıyor. Her sıçrayışta  önceki yüksekliğini %20 kaybediyor. 1 metreden daha az olana kadar aldığı toplam yolu ve sıçrama sayısını hesaplayınız?

x=float(input("yüksekliği metre cinsinde girin gir"))
if x>=1:

    sicrama=1
    alinan_yol=x*100
    while (x-x/5)*100>=100:
        x-=x/5
        alinan_yol+=2*x*100
        sicrama+=1

    print("alınan yol="+str(alinan_yol),"sıçrama="+str(sicrama))
else:
    print("yok")

#Klavyeden 3 adet kenar uzunluğu giriliyor. Girilen kenar uzunlukları göz önüne alındığında üçgenin çizilip çizilemeyeceğini, çizilebilir ise türünü (ikizkenar, çeşitkenar, eşkenar), alanını ve çevresini hesaplayan program?
#Girilen sayının Pronic (ardışık iki sayının çarpımına eşit) olup olmadığını bulunuz?

sayi=int(input("bir sayı gir"))
carpim=1
sayi_1=0
sayi_2=1
kontrol=0

while carpim<sayi:
    carpim=sayi_1*sayi_2
    if sayi==carpim:
        kontrol=1
        break
    else:
        sayi_1+=1
        sayi_2+=1
    
if kontrol==1:
    print("sayı pronic.çarpılan sayılar",sayi_1,"ve",sayi_2)
else:
    print("sayı pronic degil")
    
#N’e kadar ki Harshad (sayının kendisi rakamları toplamına bölünüyor) olanları listele? 

n=int(input("n="))
liste=[]
deger=0

for i in range(1,n):
    rak_top=0
    deger=i

    for j in range(len(str(deger))):
        rak_top+=deger%10
        deger=deger//10

    if i%rak_top==0:
        liste.append(i)

print(liste)

#Girilen sayının Jumbled (komşu rakamlar arasındaki fark maksimum 1) olup olmadığını bulunuz? 

sayi=int(input("sayı gir"))
degisken_1=0
degisken_2=0
kontrol=0

for i in range(len(str(sayi))-1):
    degisken_1=sayi%10
    sayi=sayi//10
    degisken_2=sayi%10
    if degisken_1-degisken_2==1 or degisken_2-degisken_1==1:
        continue
    else:
        kontrol=1
        break

if kontrol==0:
    print("girilen sayı jumbled")
else:
    print("girilen sayı jumbled değil")


#04.Lab

#Kullanıcıdan alınan 5 sayı içerisinden for döngüsü kullanarak en küçük sayıyı bulan programı kodlayınız.

liste=[]
for i in range(5):
    sayi=int(input("sayı girin"))
    liste.append(sayi)

min=liste[0]
for i in liste:
    if i<min:
        min=i

print(min)

#1 den 10′ a kadar sayıları tersten yani 10′ dan geriye yazdırın.

for i in range(10,0,-1):
    print(i,end=" ")

#Kullanıcıdan isim ve soyisim bilgisini alan ve bunların harf uzunluğunu bulan programı yazınız. (Kullanıcıdan aldığınız değerleri bir diziye atayarak yapınız.)

liste=[]
isim=input("isim")
soyisim=input("soyisim")
liste.append(isim)
liste.append(soyisim)
for i in liste:
    print(i+"="+str(len(i)))


#Bu listedeki üç sayıdan oluşan demetlerin (tuple) her birinin bir üçgen olup olmadığını ve hangi üçgen tipi olduğunu kontrol eden programı yazınız.
edges = [(3, 4, 5), (5, 12, 13), (2, 15, 17), (5, 5, 5), (5, 5, 8), (1, 24, 25)]


#kullanıcıdan öğrenci adını ve üç sınav notunu girmesini isteyin.Kullanıcı 'q' tuşuna basana kadar bu işlemi tekrarlansın. Ardından,
#öğrenci not bilgilerini ekrana yazdırın, her öğrencinin adını,notlarını ve ortalama notunu gösteren programı yazınız.

kontrol="a"
cikti=""

while kontrol=="a":
    ogrenci_adi=input("öğrencinin adı")
    if ogrenci_adi=="q":
        break
    not_1=int(input("1. notu girin"))
    not_2=int(input("2. notu girin"))
    not_3=int(input("3. notu girin"))
    cikti+= "öğrenci adı="+ogrenci_adi + "\nnotları="+str(not_1)+" "+str(not_2)+" "+str(not_3)+"\nortalama="+str((not_1+not_2+not_3)/3)+"\n"

print(cikti)








