# @author Jacob Sylva
# allows the user to sort through a .txt file of Kansas town names, and 
# create a new .txt file based on the letter the user inputs.

getLetter = input('Get Kansas towns beginning with which letter? ')
towns = []

# Reads data from 'Kansastowns.txt' file and appends Kansas town names if they
# match the user input.
with open('KansasTowns.txt', 'r') as inFile:
    text = inFile.readlines()
    for line in (text):
        if (line[0].lower() == getLetter.lower()):
            towns.append(line)
    towns.sort()
    
# Solves if list is empty, no towns with the user input letter exist
# Creates new .txt file with towns from KansasTowns.txt based on user selected 
# letter.
    if (len(towns) == 0):
        print(f'No Kansas towns begin with {getLetter}')
    else:
        with open(f'KansasTownsStartingWith{getLetter.upper()}', 'w') as \
             newFile:
            for listItem in towns:
                newFile.write(listItem)
        print(f'KansasTownsStartingWith{getLetter.upper()}.txt has been created')
