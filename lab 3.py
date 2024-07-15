
name=(input("enter your name :-"))
a=(input("enter your 1st c language mark :-"))
b=(input("enter your 2st python mark :-"))
c=(input("enter your 3st html mark :-"))
d=(input("enter your 4st java mark :-"))
e=(input("enter your 5st php mark :-"))
print("_______________________________________________________________________________________________________________________________")
print("\t\t\t\t\t\t\t result \t\t\t\t\t")
print("_______________________________________________________________________________________________________________________________")
print("no \t\t\t  subject \t\t total \t\t\tyour mark")
print("_______________________________________________________________________________________________________________________________")
print("1 \t\t\t  c language\t\t 100 \t\t\t",a)
print("2 \t\t\t  python\t\t 100 \t\t\t",b)
print("3 \t\t\t  html\t\t\t 100 \t\t\t",c)
print("4 \t\t\t  java\t\t\t 100 \t\t\t",d)
print("5 \t\t\t  php\t\t  \t 100 \t\t\t",e)
total=int(a)+int(b)+int(c)+int(d)+int(e)
print("_______________________________________________________________________________________________________________________________")
print("\t\t\t\t\t\t500\t\t\t",total)
total1=500
par=total/total1*100
print("_______________________________________________________________________________________________________________________________")
print("your par is:-",par)
if(int(a)<18 or int(b)<18 or int(c)<18 or int(d)<18 or int(e)<18):
    print("you are fail")
else:
    print("you are pass")
    