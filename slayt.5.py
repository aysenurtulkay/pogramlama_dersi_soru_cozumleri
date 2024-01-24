# Girilen 5 sayının ortalamasını bulan program?

top=0
for i in range(5):
    sayi=int(input("deger girin"))
    top+=sayi

print(top/5)

# Girilen 5 sayının standart sapmasını bulan program?

sayilar=[]
top=0 
toplam=0

for i in range(5):
    sayi=int(input("sayı gir"))
    sayilar.append(sayi)

for j in sayilar:
    top+=j 
ort=top/5

for k in sayilar:
    toplam+=(k-ort)**2

sonuc=(toplam/4)**0.5

print(sonuc)

# Girilen sayının listede olup olmadığını bulan program?

liste=[1,11,21,31,41,51,61,71,81,91,10]
kontrol=0
sayi=int(input("sayı gir"))

for i in liste:
    if i==sayi:
        kontrol=1

if kontrol==1:
    print("sayı listede var")
else:
    print("sayı listede yok")

# Farklı değerlere sahip iki listenin korelasyon katsayısını hesaplayan program?

x=[1,2,3,4,5,6,7]
y=[9,8,10,12,11,13,14]
carpimlarin_toplami=0
top_x=0
top_y=0
kare_top_x=0
kare_top_y=0
pay=0
payda=0

for i in range(len(x)):
    top_x+=x[i]
    top_y+=y[i]

    carpimlarin_toplami+=(x[i]*y[i])

    kare_top_x+=(x[i]**2)
    kare_top_y+=(y[i]**2)

top_x=top_x/len(x)
top_y=top_y/len(y)
carpimlarin_toplami=carpimlarin_toplami/len(x)
kare_top_x=kare_top_x/len(x)
kare_top_y=kare_top_y/len(y)

pay=carpimlarin_toplami-(top_x*top_y)
payda=((kare_top_x-(top_x**2))**0.5)*((kare_top_y-(top_y**2))**0.5)

print(pay/payda)

# Elemanları sıralayan program?

liste=[1,34,567,21,657,123,54]
liste.sort()
print(liste)

# Her elemanın tekrar sayısını bulan program?

liste=[1,2,3,34,21,343,2,1,3,3,1,4,54,7,12,1,1]
sozluk={}

for i in liste:
    degisken=0
    for j in liste:
        if i==j:
            degisken+=1
    sozluk[i]=degisken

for i in sozluk:
    print(str(i)+"="+str(sozluk[i]))

# Girilen yazıdaki boşluk karakter sayısını bulan program?

yazi=input("metin gir")

bosluk_sayisi=0
for i in yazi:
    if i==" ":
        bosluk_sayisi+=1

print(bosluk_sayisi)

# Girilen iki yazıyı karşılaştıran (eşit olup olmadığını bulan) program?

yazi_1=input("ilk yazıyı girin")
yazi_2=input("ikinci yazıyı girin")

kontrol=0
if len(yazi_1)==len(yazi_2):
    for i in range(len(yazi_1)):
        if yazi_1[i]!=yazi_2[i]:
            kontrol=1
            break
else:
    kontrol=1
    
if kontrol==0:
    print("yazılar aynı")
else:
    print("yazılar farklı")

# Girilen yazının büyük yazılıp yazılmadığını bulan program?

yazi=input(" yazı girin")

kontrol=0
for i in range(len(yazi)):
    if yazi.upper()[i]!=yazi[i]:
        kontrol=1
        break

if kontrol==0:
    print("yazı buyuk harfle yazılmış")
else:
    print("yazı kucuk harfle yazılmış")

# Girilen yazının k. karakteriyle r. karakteri arasını kopyalayan programı yazınız?

yazi=input("bir yazı girin")
k=int(input("k"))
r=int(input("r"))
yeni_yazi=""

for i in range(k,r-1):
    yeni_yazi+=yazi[i]
        
print(yeni_yazi)

# Girilen yazıdaki kelime, rakam ve karakter sayısını bulan prog<<<ram?

yazi=input("metni gir")
kelime=""
liste=[]
rakamlar="0123456789"
rakam=0

for i in range(len(yazi)):
    if yazi[i]!=" ":
        kelime+=yazi[i]
        if i==len(yazi)-1:
            liste.append(kelime)
    else:
        liste.append(kelime)
        kelime=""

    if yazi[i] in rakamlar:
        rakam+=1

kelime_sayisi=len(liste)
karakter=len(yazi)

print("kelime="+str(kelime_sayisi),"rakam="+str(rakam),"karakter="+str(karakter))

# Girilen yazıdaki aranan kelimenin önüne ve arkasına TIRNAK sembolünü ekleyen program?

yazi=input("metni gir")
aranan_kelime=input("aranan kelimeyi gir")
liste=[]
kelime=""
yeni_cumle=""

for i in range(len(yazi)):
    if yazi[i]!=" ":
        kelime+=yazi[i]
        if i==len(yazi)-1:
            liste.append(kelime)
            kelime=""
    else:
        liste.append(kelime)
        kelime=""

for i in liste:
    if i!=aranan_kelime:
        yeni_cumle+=i+" "
    else:
        yeni_cumle+="'"+i+"' "

print(yeni_cumle)

# Girilen yazıdaki bir karakteri sil

yeni_yazi=""
yazi=input("bir yazı girin")
silinecek_karakter=input("silinecek karakteri girin")

for i in yazi:
    if i!=silinecek_karakter:
        yeni_yazi+=i

print(yeni_yazi)

# Girilen yazıdaki bir kelimeyi sil

yazi=input("bir yazı girin")
silinecek_kelime=input("silinecek kelimeyi girin")
kelime=""
yeni_yazi=""
liste=[]

for i in yazi:
    if i!=" ":
        kelime+=i
        if yazi.index(i)==len(yazi)-1:
            liste.append(kelime)
    else:
        liste.append(kelime)
        kelime=""

for i in liste:
    if i!=silinecek_kelime:
        yeni_yazi+=i
        yeni_yazi+=" "

print(yeni_yazi)

# Girilen yazıdaki noktalama işaretlerini sil

noktalama_isaretleri=".:;,-_*?/+%&^'!"
yazi=input("yazı girin")
yeni_yazi=""

for i in yazi:
    if i in noktalama_isaretleri:
        yeni_yazi+=" "
    else:
        yeni_yazi+=i

print(yeni_yazi)

# Girilen onluk sayıyı ikili sayıya dönüştürünüz?

sayi=int(input("sayı gir"))
yeni_sayi=""
sonuc=""
while sayi/2>=1:
    yeni_sayi+=str(sayi%2)
    sayi=sayi//2

yeni_sayi+=str(sayi)

for i in range(len(yeni_sayi)-1,-1,-1):
    sonuc+=str(yeni_sayi[i])

print(sonuc)

# Girilen onluk sayıyı onaltılık sayıya dönüştürünüz?

sayi=int(input("sayı gir"))
liste=["A","B","C","D","E","F"]
yeni_sayi=""
sonuc=""
while sayi/16>=1:
    if sayi%16>9:
        yeni_sayi+=str(liste[sayi%16-10])
    else:
        yeni_sayi+=str(sayi%16)
    sayi=sayi//16

yeni_sayi+=str(sayi)

for i in range(len(yeni_sayi)-1,-1,-1):
    sonuc+=str(yeni_sayi[i])

print(sonuc)

# Girilen ikilik sayıyı onluk sayıya dönüştürünüz?

sayi=input("sayı gir")
yeni_sayi=""
sonuc=0
degisken=0

for i in range(len(sayi)-1,-1,-1):
    yeni_sayi+=sayi[i]

for j in yeni_sayi:
    sonuc+=(2**degisken)*int(j)
    degisken+=1

print(sonuc)




