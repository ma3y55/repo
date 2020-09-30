print("zagarjamy w gre")
import time
time.sleep(2)
print("wybierz liczbe od 1 do 10")

import random
liczba =  random.randint(1, 10)

x = input("jaka to liczba")






if liczba < int(x):
    print("za duzo")
if liczba > int(x):
    print("za mało")
if liczba == int(x):
    print("dobrze")
input("wcisnij przycisk")
