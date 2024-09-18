FILE_NAME = "namn.txt"

def spara_namn_till_fil(namn):
    with open(FILE_NAME, "a", encoding='utf-8') as f:
        f.write(namn +'\n')

def hämta_alla_sparade_namn():
    lista_med_namn = []
    with open(FILE_NAME, "r", encoding='utf-8') as f:
        for line in f:
            namn = line.strip()
            lista_med_namn.append(namn)

    return lista_med_namn

def skriv_ut_namn(lista_med_namn):
    print("####################################")
    print("########## Namn i filen ############")
    print("####################################")
    for nummer, namn in enumerate(lista_med_namn,start=1):
        print(str(nummer) + '. ' +namn)

    print("####################################")
    print("########## Slut på namn ############")
    print("####################################")

if __name__ == '__main__':
    while True:
        print("1. Lägg till namn")
        print("2. Skriv ut namn")
        print("3. Avsluta")
        val = input("Ange önskat val: ")

        if val == '1':
            namn = input("Ange namn: ")
            spara_namn_till_fil(namn)
        
        elif val == '2':
            lista_med_namn = hämta_alla_sparade_namn()
            skriv_ut_namn(lista_med_namn)

        elif val == '3':
            break

        else:
            print("Ogiltligt val! Försök igen")
        