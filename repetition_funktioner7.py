import os

def rensa_skärmen():
    if os.name == "nt":
        os.system("cls")

    elif os.name == 'posix':
        os.system('clear')


while True:
    data = input("Skriv 'rensa' för att rensa skärmen!")
    
    if data == "rensa":
        rensa_skärmen()

    elif data == "q":
        rensa_skärmen()
        break

    else:
        print(data)
