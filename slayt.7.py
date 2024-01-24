#Matrissel İşlemler
import random
#İki matrisin toplamını bul.

def matris_yaz(matris,ad):
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()
    print()

matris_1=[[round(random.random()*10)for x in range(3)] for x in range(3)]
matris_2=[[round(random.random()*10)for x in range(3)] for x in range(3)]
toplam_matrisi=[[0 for x in range(3)]for x in range(3)]

for i in range(len(matris_1)):
    for j in range(len(matris_1[i])):
        toplam_matrisi[i][j]=matris_1[i][j]+matris_2[i][j]
    print()

matris_yaz(matris_1,"matris 1")
matris_yaz(matris_2,"matris 2")
matris_yaz(toplam_matrisi,"matrislerin toplamı")

#Matrisin satır ve sütun toplamlarını hesapla.

matris=[[round(random.random()*10)for x in range(3)]for x in range(3)]

def matrisyaz(matris):
    print("matris")
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()
    print()
    
def satir(matris):
    for i in range(len(matris)):
        satir_top=0
        for j in range(len(matris[i])):
            satir_top+=matris[i][j]
        print("satır",i+1,"toplamı",satir_top)

def sutun(matris):
    for i in range(len(matris)):
        sutun_top=0
        for j in range(len(matris[i])):
            sutun_top+=matris[j][i]
        print("sütun",i+1,"toplamı",sutun_top)

matrisyaz(matris)
satir(matris)
sutun(matris)

#Matristeki en büyük sayıyı bul.

matris=[[round(random.random()*10)for x in range(3)]for x in range(3)]

def matris_yaz1(matris):
    print("matris")
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()
    print()

def en_buyuk(matris):
    en_b=matris[0][0]
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            if en_b<matris[i][j]:
                en_b=matris[i][j]
    print("en büyük değer",en_b)

matris_yaz1(matris)
en_buyuk(matris)

#Matris izini (diyagonal toplam) bul.

matris=[[round(random.random()*10)for x in range(3)]for x in range(3)]

def matris_yaz2(matris):
    print("matris")
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()
    print()

def diyagonal_toplam(matris):
    di_top=0
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            if i==j:
                di_top+=matris[i][j]
    print(di_top)

matris_yaz2(matris)      
diyagonal_toplam(matris)   

#Verilen sayıyı matrisin k. indeksine yerleştir?

matris=[[round(random.random()*10)for x in range(3)]for x in range(3)]
sayi=int(input("bir sayı girin"))
indeks=int(input("0-8 arası bir indeks gir"))

def matris_yaz3(matris):
    print("matris")
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()
    print()

def matris_degis(matris,indeks,sayi):
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            if (i*len(matris[i])+j)==indeks:
                matris[i][j]=sayi
    print(str(indeks)+". indeksin",sayi,"ile değiştirilmesi ile oluşan matris")
    matris_yaz3(matris)

matris_yaz3(matris)
matris_degis(matris,indeks,sayi)

#Matrisin transpozunu alın.
#cozum-1

sutun=random.randint(3,5)
satir=random.randint(3,5)

matris=[[random.randint(0,9)for x in range(sutun)]for x in range(satir)]

def matris_yazdir(matris,ad):
    result = ad + "\n"
    for i in range(len(matris)):
        for k in range(len(matris[i])):
            result+=str(matris[i][k])+" "
        result += "\n"
    return result
    
def transpoz(matris):
    yeni_matris=[[0 for x in range(len(matris))]for x in range(len(matris[0]))]
    for i in range(len(matris)):
        for k in range(len(matris[i])):
            yeni_matris[k][i]=matris[i][k]
    return yeni_matris

print(matris_yazdir(matris,"matris"))
print(matris_yazdir(transpoz(matris),"transpozu"))

#cozum-2

sutun=random.randint(3,5)
satir=random.randint(3,5)
matris=[[random.randint(0,9)for x in range(sutun)]for x in range(satir)]

def matris_yazdir(matris,ad):
    print(ad)
    for i in range(len(matris)):
        for k in range(len(matris[i])):
            print(matris[i][k],end=" ")
        print()

def transpoz(matris):
    yeni_matris=[[0 for x in range(len(matris))]for x in range(len(matris[0]))]
    for i in range(len(matris)):
        for k in range(len(matris[i])):
            yeni_matris[k][i]=matris[i][k]
    return yeni_matris

(matris_yazdir(matris,"matris"))
(matris_yazdir(transpoz(matris),"transpozu"))

#İki matrisin çarpımını hesaplayan prog?

matris_1=[[random.randint(1,5)for x in range(3)]for x in range(3)]
matris_2=[[random.randint(1,5)for xi in range(3)]for x in range(3)]
matris_sonuc=[[0 for x in range(3)]for x in range(3)]

def matris_yazdir1(matris,ad):
    print(ad)
    for i in range(3):
        for k in range(3):
            print(matris[i][k],end=" ")
        print()

def matris_carpim(matris1,matris2):
    for i in range(3):
        for j in range(3):
            top=0
            for k in range(3):
                top+=matris1[i][k]*matris2[k][j]
                matris_sonuc[i][j]=top
    return matris_sonuc

matris_yazdir1(matris_1,"matris 1")
matris_yazdir1(matris_2,"matris 2")
matris_yazdir1(matris_carpim(matris_1,matris_2),"carpimlari")

#Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.
#cozum-1

def matris_yaz3(matris):
    print("matris")
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()
    print()

n=int(input("bir n degeri girin"))
matris=[[0 for x in range(n)]for x in range(n)]

def n_yerlestir(matris):
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            matris[i][j]=i*len(matris[i])+j+1
    print(matris_yaz3(matris))

n_yerlestir(matris)

#cozum-2

def matris_yaz3(matris):
    print("matris")
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()
    print()

def n_yerlestir1(n):
    degisken=1
    matris=[[0 for x in range(n)]for x in range(n)]
    for i in range(n):
        for j in range(n):
            matris[i][j]=degisken
            degisken+=1
    matris_yaz3(matris)

n=int(input("bir n degeri girin"))
n_yerlestir1(n)

#0-1 değerlerini içeren bir matristeki nesnenin alanını hesapla.

matris=[[random.randint(0,1)for x in range(4)]for x in range(4)]

def matris_yazz(matris):
    for i in range(len(matris)):
        for k in range(len(matris[i])):
            print(matris[i][k],end=" ")
        print()

def nesne_alani(matris):
    toplam=0
    for i in range(len(matris)):
        for k in range(len(matris[i])):
            if matris[i][k]==1:
                toplam+=1
    return toplam

matris_yazz(matris)
print(nesne_alani(matris))

#0-1 değerlerini içeren bir matristeki nesnenin kenarlarını hesapla. 

matris=[[random.randint(0,1)for x in range(4)]for x in range(4)]

def matris_yazz(matris):
    for i in range(len(matris)):
        for k in range(len(matris[i])):
            print(matris[i][k],end=" ")
        print()

def matris_kenar(giris):
    kenar_sayisi=0
    for i in range(len(matris)):
        for k in range(len(matris[i])):
            if matris[i][k]==1:
                if i==0 or matris[i-1][k]==0:
                    kenar_sayisi+=1
                if k==0 or matris[i][k-1]==0:
                    kenar_sayisi+=1
                if i==len(matris)-1 or matris[i+1][k]==0:
                    kenar_sayisi+=1
                if k==len(matris[i])-1 or matris[i][k+1]==0:
                    kenar_sayisi+=1

    return kenar_sayisi

matris_yazz(matris)
print(matris_kenar(matris))

#Matristeki şekli n kat büyüten programı yazınız?

matris=[[random.randint(1,5)for x in range(3)]for x in range((3))]

n=int(input("n değerini gir"))
yeni_matris=[[0 for x in range(3*n)]for x in range((3*n))]

def matris_yazz(matris):
    for i in range(len(matris)):
        for k in range(len(matris[i])):
            print(matris[i][k],end=" ")
        print()

def matris_buyut(matris,n):
    for i in range(3*n):
        for j in range(3*n):
            yeni_matris[i][j]=matris[i//n][j//n]
                
matris_yazz(matris)
matris_yazz(matris_buyut(matris,n))