data = ["Avi", "Anita", "Ida", "Maanvi", "Ruban", "Rupal", "Sanajana", "Veer"]

key = input("Who are you looking for (Please start with a capital letter)?: ")

for i in range(0, len(data)):
    print(data[i])
    if key == data[i]:
        print("^^^The Contact has been found: ({})".format(key))