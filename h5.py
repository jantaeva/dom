class Person:
    pass

a=Person()
b=Person()
b.arg=input("Your name please:   ")
a.arg=int(input("how old are you?   "))
if a.arg in range(1,6):
    print(b.arg,"vam v det sad")
if a.arg in range(6,17):
   print(b.arg,"vam v shkolu")
if a.arg in range(17,25):
   print(b.arg,"vam v VUZ")
if a.arg in range(25,60):
   print(b.arg,"vam na rabotu")
if a.arg in range(60,120):
   print(b.arg,"vam na otdyh")
