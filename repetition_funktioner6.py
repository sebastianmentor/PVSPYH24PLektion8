def är_sträng_en_float(sträng):
    """Kontrollera om en sträng kan konverteras till int eller float"""
    # Om strängen är tom så är den inte en giltlig float
    if sträng == '':
        return False

    # kollar om det är ett heltal eller ett negativt heltal
    if sträng.isdigit() or (sträng[0]=='-' and sträng[1:].isdigit()):
        return True
    
    # kollar om det finns en punkt i strängen
    elif '.' in sträng:
        # eventuellt negativ float
        if sträng[0] == '-':
            # tar bort minustecknet
            sträng = sträng[1:]

        # delar strängen på . för att se om vi får två delar!
        # exempel: 5.4 -> [5, 4] | 5.4.1 -> [5, 4, 1]  
        möjlig_float_lista = sträng.split(".")
        
        if len(möjlig_float_lista) == 2:
            # kollar så att båda delarna om punkt är heltal
            if möjlig_float_lista[0].isdigit() and möjlig_float_lista[1].isdigit():
                return True
    
    return False
    


while True:
    sträng = input("Vänligen mata in en float: ")
    är_en_float = är_sträng_en_float(sträng)
    
    if är_en_float:
        print("Bra! Du matade in en giltlig float!")
    elif sträng == "q":
        break
    else:
        print(f"Ogiltlig inmatning! {sträng} kan inte konverteras till sträng")
