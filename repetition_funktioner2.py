def min_funktion(attributet):
    print("Hej från min_funktion!")
    print("Tack för att du anroppa mig!")
    print("Jag ska nu skriva ut vilken typ och värde på vad du skicka in till mig.")
    print("Typen är av attributet är", type(attributet), "och värdet är", attributet)
    print()


min_funktion("Hejsan")
min_funktion(42)
min_funktion(min_funktion)
min_funktion(input("Skriv något: "))