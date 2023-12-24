#02. Matematiksel İşlemler

#Girilen iki sayıyı toplayıp sonucunu ekrana yazdıran program?
sayi_1=int(input("ilk sayıyı giriniz"))
sayi_2=int(input("ikinci sayıyı giriniz"))
print(sayi_1,"ve",sayi_2,"sayılarının toplamı",sayi_1+sayi_2)

#V=I*R formülünü kullanarak verilen I ve R değerine göre V yi hesaplayan prog?
i=int(input("I değerini girin"))
r=int(input("R değerini girin"))
print("v değeri",i*r)

#Kısa ve uzun kenarı girilen dikdörtgenin alanını ve çevresini  hesaplayan prog?
kisa_kenar=int(input("kısa kenarı giriniz"))
uzun_kenar=int(input("uzun kenarı giriniz"))
print("alan",kisa_kenar*uzun_kenar,"\nçevre",2*(kisa_kenar+uzun_kenar))

##Yarıçapı verilen çemberin alanını hesaplayan prog (pi = 3,14)?
yari_cap=int(input("yarıçapı giriniz"))
print("alan",3.14*(yari_cap**2))

#Girilen gün sayısını kaç yıl ve kaç ay olduğunu bulan program?
giris=int(input("gün sayısı giriniz"))
yil=giris//365
ay=(yil%365)//30
gun=(giris-yil*365)%30
print(yil,"yıl",ay,"ay",gun,"gün")

#Girilen 3 basamaklı bir sayıyı tersine çeviren program? (573 ==> 375)
sayi=int(input("bir sayı giriniz"))
bir=sayi%10
on=(sayi-bir)%100
yuz=sayi//100
print(bir*100+on+yuz)

#100'lük sistemde notu girilen öğrencinin notunu 5'lik sisteme çeviriniz?
ogrnotu=int(input("notunuzu giriniz"))
print(ogrnotu/20)

#Fiyat ve kdv oranı girilen ürünün toplam fiyatını ekrana yazdıran program?
fiyat=int(input("fiyatı giriniz"))
kdv=int(input("kdv yüzde kaç"))
print(fiyat+(fiyat*kdv)/100)

#Bir ürünün alış fiyatı, vergi ve kar oranlarını kullanılarak satış fiyatını hesaplayan program?
alis_fiyati=int(input("alış fiyatını giriniz"))
vergi=int(input("vergi oranı yüzde kaç giriniz"))
kar_orani=int(input("kar oranıyüzde kaç giriniz"))
print("satış fiyatı",alis_fiyati*100/(100-vergi-kar_orani))

#Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran program?
sayi=int(input("bir sayı giriniz"))
bir=sayi%10
on=(sayi-bir)%100
yuz=sayi//100
print("yüzler basamğı",yuz*100,"onlar basamağı",on,"birler basamağı",bir)

#A ve B değişken değerlerini üçüncü bir değişken kullanmadan yer değiştiriniz?
a=int(input("bir sayı giriniz"))
b=int(input("bir sayı giriniz"))
a+=b
b=a-b
a-=b
print("a="+str(a),"b="+str(b))

#Girilen n ve k değerlerine göre k + 2k + 3k + ...+nk yı hesaplayan program?  
n=int(input("n değerini giriniz"))
k=int(input("k değerini giriniz"))
print(n*(n+1)*k/2) 

#Çizginin başlangıç ve orta nokta koordinatları veriliyor. Diğer uç noktanın koordinatlarını bulunuz?
x_1=int(input("ilk noktanın x değerini giriniz"))
y_1=int(input("ilk noktanın y değerini giriniz"))
x_2=int(input("ikinci noktanın x değerini giriniz"))
y_2=int(input("ikinci noktanın y değerini giriniz"))
x_ort=(x_1+x_2)/2
y_ort=(y_1+y_2)/2
print("orta noktanın kıoordinatları",str(x_ort)+","+str(y_ort))

#02.Lab

#Kullanıcının girdiği bir sayının hem 2'ye hemde 3'e bölünebilme durumunu kontrol eden programı kodlayınız.
sayi=int(input("bir sayı giriniz"))
if sayi%2==0 and sayi%3==0:
    print(sayi,"sayısı hem 2'ye hem 3'e tam bölünür.")
elif sayi%2==0:
    print(sayi,"sayısı 2'ye tam bölünür,3'e tam bölünmez.")
elif sayi%3==0:
    print(sayi,"sayısı 3'e tam bölünür,2'ye tam bölünmez.")

#Bir kredi kartından 2000 TL üzeri alış veriş yapıldığında 100 TL hediye puan, 1000 TL ve üzeri alış veriş yapıldığında 50 TL hediye puan,
#1000 TL’nin altında alış veriş yapıldığında 10 TL hediye puan kazanılmaktadır. Klavyeden girilen harcama tutarına göre hediye puanı yazan problemin Python kodlarını yazınız
harcama=int(input("harcama tutarını giriniz"))
if harcama>=2000:
    print("100tl hediye puan kazandınız.")
elif harcama>=1000:
    print("50tl hediye puan kazandınız.")
else:
    print("10tl hediye puan kazandınız.")

#Bir internet satış sitesi alışveriş tutarı 50 TL’nin üzerindeki her kargoyu bedava veriyor. 50 TL altı sipariş tutarına ise 7 TL ilave
#edilerek, ekrana kargo ücretini ve toplam tutarı yazdırıyor. Bu programın Python kodunu oluşturunuz.
harcama=int(input("harcama tutarını giriniz"))
if harcama>=50:
    print("kargo bedava,tutar:"+str(harcama))
else:
    print("kargo dahil toplam tutar:"+str(harcama+7))

#Bir kişiye ait cinsiyet, boy ve kilo bilgilerini alarak aşağıdaki şartlara görekişinin ideal kiloda olup olmadığını, 
#ideal kiloda değilse kaç kilo alması veya kaç kilo vermesi gerektiğini bulan Python kodunu oluşturunuz.
# İdeal Kilo Hesabı: Bayanlarda: Boy-110, Erkeklerde: Boy-108
cinsiyet=int(input("cinsiyet seçiminde aşağıdaki bilgilere göre seçim yapınız.\nkadın=1\nerkek=0\ncinsiyet="))
boy=int(input("boy="))
kilo=int(input("kilo="))
if cinsiyet==1:
    if kilo>(boy-110):
        print("ideal kiloya ulaşmak için",kilo-(boy-110),"kilo vermelisiniz.")
    elif kilo==(boy-110):
        print("ideal kilodasınız.")
    else:
        print("iddeal kiloya ulaşmak için",(boy-110)-kilo,"almalısınız.")
elif cinsiyet==0:
    if kilo>(boy-108):
        print("ideal kiloya ulaşmak için",kilo-(boy-108),"kilo vermelisiniz.")
    elif kilo==(boy-108):
        print("ideal kilodasınız.")
    else:
        print("iddeal kiloya ulaşmak için",(boy-108)-kilo,"almalısınız.")
else:
    print("yanlış giriş yaptınız.")

#Kullanıcıya Python ya da Java programlama dillerini ve İngilizce dilini bilip bilmediğini soran, Python ya da Javadan birini biliyorsa ve
#İngilizce dilini biliyorsa “İş alım süreciniz olumlu geçti”, değilse “Aranan pozisyona nitelikleriniz uymamaktadır.” mesajı veren Python kodunu oluşturunuz.
kod=int(input("python ya da java programlama dillerinden en az birini biliyorsaız '1' tuşuna,ikisni de bilmiyorsanz '0' tuşuna basınız."))
dil=int(input("ingilizce biliyorsanız '1' tuşuna,bilmiyorsanz '0' tuşuna basınız."))
if kod==1 and dil==1:
    print("İş alım süreciniz olumlu geçti")
elif kod==0 or dil==0:
    print("Aranan pozisyona nitelikleriniz uymamaktadır.")
else:
    print("yanlış giriş yaptınız.")

#Bir mağaza müşterilerine yaptıkları alışveriş tutarına göre indirim yapmaktadır. 200 TL ye kadar olan alışverişler için %10,
#200-400 TL arası olan alışverişler için %15, 400 TL den fazla olan alışverişler için %20 olacak şekilde indirim yapıp alışveriş tutarını yazan Python kodunu oluşturunuz.
harcama=int(input("toplam alışveriş tutarını giriniz."))
if harcama>=400:
    print("indirimli alışveriş tutarı="+str(harcama/100*80))
elif harcama>=200:
    print("indirimli alışveriş tutarı="+str(harcama/100*85))
else:
    print("indirimli alışveriş tutarı="+str(harcama/100*90))

#Klavyeden, girilen ay bilgisine göre kuzey yarım kürede hangi mevsimin yaşandığını ekrana yazdıran Python kodunu oluşturunuz.
ay=int(input("aşağıda verilenlere göre hangi ayda olduğunuzu seçin:\n1=ocak\n2=şubat\n3=mart\n4=nisan\n5=mayıs\n6=haziran\n7=temmuz\n8=ağustos\n9=eylül\n10=ekim\n11=kasım\n12=aralık\n"))
if ay==12 or ay==1 or ay==2:
    print("mevsim kış")
elif ay==3 or ay==4 or ay==5:
    print("mevsim ilkbahar")
elif ay==6 or ay==7 or ay==8:
    print("mevsim yaz")
elif ay==9 or ay==10 or ay==11:
    print("mevsim sonbahar")
else:
    print("yanlış giriş yaptınız")

#Kullanıcının girdiği üç sayı arasındaki en küçük çift sayıyı bulun veya eğer hiç çift sayı yoksa bir mesaj yazdırın.
sayi_1=int(input("ilk sayıyı giriniz"))
sayi_2=int(input("ikinci sayıyı giriniz"))
sayi_3=int(input("üçüncü sayıyı giriniz"))
if sayi_1%2==0 and sayi_2%2==0 and sayi_3%2==0:
    if sayi_1<sayi_2 and sayi_1<sayi_3:
        print("en küçük çift sayı",sayi_1)
    elif sayi_2<sayi_1 and sayi_2<sayi_3:
        print("en küçük çift sayı",sayi_2)
    else:
        print("en küçük çift sayı",sayi_3)
elif sayi_1%2==0 and sayi_2%2==0:
    if sayi_1>sayi_2:
        print("en küçük çift sayı",sayi_2)
    else:
        print("en küçük çift sayı",sayi_1)
elif sayi_3%2==0 and sayi_2%2==0:
    if sayi_3>sayi_2:
        print("en küçük çift sayı",sayi_2)
    else:
        print("en küçük çift sayı",sayi_3)
elif sayi_1%2==0 and sayi_3%2==0:
    if sayi_1>sayi_3:
        print("en küçük çift sayı",sayi_3)
    else:
        print("en küçük çift sayı",sayi_1)
elif sayi_1%2==0:
    print("en küçük çift sayı",sayi_1)
elif sayi_2%2==0:
    print("en küçük çift sayı",sayi_2)
elif sayi_3%2==0:
    print("en küçük çift sayı",sayi_3)
else:
    print(sayi_1,sayi_2,sayi_3,"sayıları arasında çift sayı yok")
