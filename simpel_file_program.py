import os

FILE_NAME = "namn_och_stad.txt"

def spara_namn_och_stad_till_fil(namn, stad):
    with open(FILE_NAME, "a", encoding='utf-8') as f:
        f.write(namn +' ' + stad + '\n')

def hämta_alla_sparade_namn_och_städer():
    lista_med_namn_och_stad = []
    with open(FILE_NAME, "r", encoding='utf-8') as f:
        for line in f:
            namn_och_stad = line.strip()
            namn, stad = namn_och_stad.split()
            lista_med_namn_och_stad.append((namn, stad))

    return lista_med_namn_och_stad

def skriv_ut_namn(lista_med_namn_och_städer):
    print("####################################")
    print("########## Namn i filen ############")
    print("####################################")

    for nummer, namn_och_stad in enumerate(lista_med_namn_och_städer, start=1):
        namn, stad = namn_och_stad
        print(str(nummer) + '. ' + namn + ' ' + stad)

    print("####################################")
    print("########## Slut på namn ############")
    print("####################################")

if __name__ == '__main__':
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding='utf-8') as f:
            pass

    while True:
        print("1. Lägg till namn och stad")
        print("2. Skriv ut namn")
        print("3. Avsluta")
        val = input("Ange önskat val: ")

        if val == '1':
            namn = input("Ange namn: ")
            stad = input("Ange stad: ")

            spara_namn_och_stad_till_fil(namn, stad)
        
        elif val == '2':
            lista_med_namn = hämta_alla_sparade_namn_och_städer()
            skriv_ut_namn(lista_med_namn)

        elif val == '3':
            break

        else:
            print("Ogiltligt val! Försök igen")
        