def kontrollera_om_värdet_är_int(värdet):
    if type(värdet) == int:
        return True
    else:
        return False


print(kontrollera_om_värdet_är_int(5))
print(kontrollera_om_värdet_är_int(5.0))
print(kontrollera_om_värdet_är_int("5"))

något_värde = 5

värde_är_int = kontrollera_om_värdet_är_int(något_värde)

if värde_är_int:
    print("Värdet var en integer!")
else: 
    print("Värdet var inte en integer!")

