name=(input("enter your name :- "))
a=(input("enter your seo mark "))
b=(input("enter your java mark "))
c=(input("enter your html mark "))
d=(input("enter your php mark "))
e=(input("enter your python mark "))
print("______________________________________________________________________________________________________________________________")
print("\t\t\t\t\t  result  \t\t\t\t\t")
print("______________________________________________________________________________________________________________________________")
print(" no. \t\t\t   subject \t\t\t total mark \t\t\t  your mark ")
print("______________________________________________________________________________________________________________________________")
print(" 1    \t\t\t   seo   \t\t\t  100   \t\t\t   ",   a)
print(" 2    \t\t\t   java   \t\t\t  100   \t\t\t   ",   b)
print(" 3    \t\t\t   html   \t\t\t  100   \t\t\t   ",   c)
print(" 4    \t\t\t   php   \t\t\t  100   \t\t\t   ",   d)
print(" 5    \t\t\t   python   \t\t\t  100   \t\t\t   ",   e)
total=int(a)+int(b)+int(c)+int(d)+int(e)
print("______________________________________________________________________________________________________________________________")
print("\t\t\t\t\t\t\t  500\t\t\t\t  ", total)
total1=500
par=total/total1*100
print("______________________________________________________________________________________________________________________________")
print("your par is-- ",par)
if( par < 100 and par > 80 ):
    print('grade a')
elif( par < 80 and par > 60):
    print('grade b')
elif( par < 60 and par > 40):
    print('grade c')
elif(par < 40 and par > 30):
    print('grade d')
else:
     print('you are not pass')
    
if(int(a)<18 or int(b)<18 or int(c)<18 or int(d)<18 or int(e)<18):
	print("you are fail")
else:
	print("your pass")
