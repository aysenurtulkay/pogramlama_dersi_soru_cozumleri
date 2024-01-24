# Aşağıdaki çıktıyı veren programı yazınız?

def faktoriyel_sekil(sayi):
    cikti="0! = 1\n"
    carpim=1
    for i in range(1,sayi+1):
        carpim*=i
        cikti+=str(i)+"! = "+str(carpim)+"\n"

    return cikti

# İlk N asal sayısını listeleyen program?

def ilk_n_asal_sayi(sayi):
    toplam=0
    degisken=2
    liste=[]

    while toplam<sayi:
        kontrol=0
        for i in range(2,degisken):
            if degisken%i==0:
                kontrol=1

        if kontrol==0:
            liste.append(degisken)
            toplam+=1

        degisken+=1

    return liste

# Girilen sayının kaç faktöriyel olduğunu bulunuz (720=6!)

def kac_faktoriyel(sayi):
    carpim=1
    degisken=1
    
    if sayi==1:
        return "sayı 0! ya da 1!"

    while carpim<sayi:
        carpim*=degisken
        if carpim==sayi:
            return degisken
        degisken+=1

print(kac_faktoriyel(1))

# Listede en fazla tekrar eden elemanı silen program?

liste=[1,2,3,34,21,343,2,1,3,3,1,4,54,7,12,1,1]
yeni_liste=[]
sozluk={}

for i in liste:
    degisken=0
    for j in liste:
        if i==j:
            degisken+=1
    sozluk[i]=degisken

max=0
degisken=0

for i in sozluk:
    if sozluk[i]>max:
        max=sozluk[i]
        degisken=i

for k in range(len(liste)):
    if liste[k]!=degisken:
        yeni_liste.append(liste[k])

print(yeni_liste)

# e uzeri x sorusu

def e_uzeri(sayi):
    toplam=0
    carpim=1
    pay=0
    payda=1

    for i in range(11):
        pay=sayi**i
        for j in range(1,sayi+1):
            payda*=j
        toplam+=pay/payda

    return toplam

print(e_uzeri(3))

# Girilen sayının Güçlü (1! + 4! + 5!  = 1 + 24 + 120 = 145) olup olmadığını bulan program?

def guclu_sayi(sayi):
    toplam=0
    for i in str(145):
        carpim=1
        for j in range(1,int(i)+1):
            carpim*=j
        toplam+=carpim

    if toplam==sayi:
        return "guclu sayi"
    else:
        return "guclu sayi degil"

# PASCAL üçgeninin n. satırını üretiniz?

pay=0
payda=0
def pascal_tek_satir(n):

    def faktoriyel(sayi):
        carpim=1
        for i in range(1,sayi+1):
            carpim*=i
        return carpim

    pay=faktoriyel(n-1)

    for i in range(n):
        payda=faktoriyel(n-1-i)*faktoriyel(i)
        print(int(pay/payda),end=" ")

# n satırlı PASCAL üçgenini çıktı veren programı yazınız?

pay=0
payda=0
def pascal_sekil(sayi):

    def faktoriyel(sayi):
        carpim=1
        for i in range(1,sayi+1):
            carpim*=i
        return carpim

    for n in range(sayi):
        pay=faktoriyel(n)
        print(" "*(sayi-n),end="")
        for r in range(n+1):
            payda=faktoriyel(n-r)*faktoriyel(r)
            print(int(pay/payda),end=" ")
        print()


