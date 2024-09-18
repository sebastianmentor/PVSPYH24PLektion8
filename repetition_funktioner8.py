import time

meny_ett_counter = 0
meny_två_counter = 0

def meny_ett():
    global meny_ett_counter
    print("Meny 1 antalr anrop", meny_ett_counter)
    meny_ett_counter =+ 1
    while True:
        print("1. Val 1")
        print("2. Val 2")
        print("3. Meny 2")
        print("4. Avsluta")
        val = input('Skriv ett val: ')

        if val == '1': 
            print('Val 1')

        elif val == '2': 
            print('Val 2')

        elif val == '3': 
            # Vi har valt 3
            menu_två() # <- när den är klar kommer vi tillbaka hit

        elif val == '4': 
            print('Programmet avslutas om:')
            for i in range(5,0,-1):
                print(f"{i}")
                time.sleep(1)
            break   

    meny_ett_counter =+ 1

def menu_två():
    global meny_två_counter
    print("Här kommer meny 2!")
    print("Meny 2 antal anrop", meny_två_counter)
    meny_två_counter =+ 1
    while True:
        print("A. Val A")
        print("B. Val B")   
        print("C. Val C")
        print("D. Avsluta")
        val = input('Skriv ett val: ').lower()

        if val == 'a': 
            print('Val A')

        elif val == 'b': 
            print('Val B')

        elif val == 'c': 
            print('Val C')

        elif val == 'd': 
            print('Meny två avslutas om:')
            for i in range(5,0,-1):
                print(f"{i}")
                time.sleep(1)     
            print('Hejdå!')
            time.sleep(2)
            break

    meny_två_counter =- 1

if __name__ == "__main__":
    meny_ett()