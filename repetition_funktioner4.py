def skriv_ut_namn_x_gånger(namn, x):
    if type(namn) == str and type(x) == int:
        print(namn*x)
    else:
        print("Ogiltliga parametrar! Skicka in rätt attributvärden")


skriv_ut_namn_x_gånger("Sebastian",4)
skriv_ut_namn_x_gånger(9,4)
skriv_ut_namn_x_gånger(9,"Kalle")
