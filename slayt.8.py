#08. Döngüsel İşlemler-2
#soru-1

#matris cozum

def matris_yaz(matris,ad):
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()

matris=[[0 for x in range(10)]for x in range(10)]
for i in range(10):
    for j in range(10):
        matris[i][j]=(i+1)*(j+1)

matris_yaz(matris,"matris")

#cozum-2

sayi=0
for i in range(1,11):
    for j in range(1,11):
        sayi=i*j
        print(sayi,end=" ")
    print()

#soru-2

def sekil_2(sayi):
    degisken=0
    for i in range(sayi+2):
        for j in range(sayi+2):
            if i==0:
                print("  ",end="  ")
                for k in range(1,sayi+1):
                    print(k,end="   ")
                break
            elif i==1:
                print("  "+"+"+"-"*sayi*4)
                break
            else:
                if j==0:
                    degisken+=1
                    print(degisken,end=" ")
                elif j==1:
                    print("|",end=" ")
                else:
                    cikti=(i-1)*(j-1)
                    print("{0:2}".format(cikti),end="  ")
        print()

#soru-3

def sekil_3(sayi):
    for i in range(sayi):
        print("*"*sayi)

#soru-4

def sekil_4(sayi):
    for i in range(1,sayi+1):
        print("*"*i)

#soru-5

def sekil_5(sayi):
    for i in range(1,sayi+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

#soru-6

def sekil_6(sayi):
    degisken=0
    for i in range(1,sayi+1):
        degisken+=1
        print(str(degisken)*i)

#soru-7

def sekil_7(sayi):
    for i in range(sayi,1,-1):
        print(str(i)*i)
    for i in range(1,sayi+1):
        print(str(i)*i)

#soru-8

def sekil_8(sayi):
    degisken=0
    for i in range(sayi):
        for j in range(1,i+1):
            degisken+=1
            print(degisken,end="")
        print()

#soru-9

def sekil_9(sayi):
    degisken=0
    for i in range(sayi):
        for j in range(sayi):
            degisken+=1
            print(degisken,end=" ")
        print()

#soru-10

def sekil_10(sayi):
    print(" "*sayi+"*")
    bosluk=sayi-1
    ara=1
    
    for i in range(sayi):
        print(" "*int(bosluk)+"*"+" "*ara+"*")
        bosluk-=1
        ara+=2

