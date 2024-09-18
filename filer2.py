# Skapar en lista med [0,1,...8,9]!!!
list_of_numbers =  []
for i in range(10):
    list_of_numbers.append(i)

# Vi kan skriva kod som tex loopar igenom något och 
# vi kan då skriva varje objekt för sig till filen
with open('my_file2.txt', 'w') as f:
    for number in list_of_numbers:
        f.write(f'{number}->{number**2}->{number**3}->{number**4}\n')