import turtle

def rita_triangel(sidlängd):
    for _ in range(3):
        turtle.forward(sidlängd)  # Flytta sköldpaddan framåt
        turtle.right(120)  # Vrid sköldpaddan 120 grader åt höger

def rita_kvadrat(sidlängd):
    for _ in range(4):
        turtle.forward(sidlängd)  # Flytta sköldpaddan framåt
        turtle.right(90)  # Vrid sköldpaddan 90 grader åt höger

def rita_femhörning(sidlängd):
    for _ in range(5):
        turtle.forward(sidlängd)  # Flytta sköldpaddan framåt
        turtle.right(72)  # Vrid sköldpaddan 72 grader åt höger

def rita_hexagon(sidlängd):
    for _ in range(6):
        turtle.forward(sidlängd)  # Flytta sköldpaddan framåt
        turtle.right(60)  # Vrid sköldpaddan 60 grader åt höger

def ritan_n_hörning(sidlängd, antal_sidor):
    rotering = 360/antal_sidor

    for _ in range(antal_sidor):
        turtle.forward(sidlängd)  # Flytta sköldpaddan framåt
        turtle.right(rotering)  # Vrid sköldpaddan 60 grader åt höger

# Skapa turtle-fönster och ställ in hastighet
turtle.speed(3)

# Anropa funktionen för att rita en kvadrat med sidan 100 pixlar
rita_kvadrat(100)
rita_triangel(100)

rita_femhörning(100)
rita_hexagon(100)

turtle.forward(200)
ritan_n_hörning(100,3)
ritan_n_hörning(100,4)
ritan_n_hörning(100,5)
ritan_n_hörning(100,6)


# Stäng fönstret vid klick
turtle.exitonclick()
