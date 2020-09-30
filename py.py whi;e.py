

while True:
    m = input("\t\t\t MENU \n"
              "\t 1. STAN KONTA \n "
              "\t 2. WPŁATA GOTÓWKI \n"
              "\t 3. WYPŁAĆ GOTÓWKĘ \n"
              "\t 4. KREDYT GOTÓWKOWY \n"
              "\t 5. WYJDŹ:\n")
    str(m)


    # stan konta
    if m == '1':

        print("Stan twojego konta" )
        s = 5000
        float(s)

        print(s)


    #wyplata
    if m == '2':
        print("Wypłata Gotówki")





    #wpłata
    if m == '3':
        print("Wpłata gotówki")


    #kredo
    if m == '4':
        print(" kredyty")

    #exit
    if m == '5':
        print("wyjdz")

    #error
    else:
        print("błąd")
        import os
        os.system("CLS")




input("wcisnij enter")