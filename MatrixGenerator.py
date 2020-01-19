import webbrowser


def info():
    info = [
        "\n\n",
        "###  Matrix Generator  ###",
        "###  © July 2019 by Eric J Lein\n",
        "###  Generates a 12-Tone Matrix from a tone row.",
        "###  A 12-tone Matrix is a grid of numbers representing musical pitches.",
        "###  Traditionally, all 12 pitches may be represented once and only once.",
        "###  This generator allows for repetitions and any given row length.",
        "###  Rows left to right are Prime.",
        "###  Rows right to left are Retrograde.",
        "###  Columns Top to Bottom are Inversion.",
        "###  Columns Bottom to Top are Retregrade Inversion.",
        "###  Accepts all integers.",
        "###  Accepts T/t for 10 and E/e for 11.",
        "###  Works for any size row.",
        "###  Outputs 10 as T and 11 as E.",
        "###  'Re' at any time time restart",
        "###  More info can be found on Wikipedia. Would you like to be redirected?",
        "###  'Wiki' at any time to redirect. Enter to start. 'Info' to reread."
    ]

    for sentence in info:
        print(sentence)


info()

def wiki():
    webbrowser.open("https://en.wikipedia.org/wiki/Twelve-tone_technique")

wikiInp = input().lower()
if wikiInp == "wiki":
    print("\n\n")
    wiki()
elif wikiInp == "info":
    print("\n\n")
    info()



def getRow():
    
    tone_row = []
    matrix = []
    tone_row = input("\n\nEnter row as space separated integers:\nTone Row = ")
    
    if tone_row.lower() == "wiki":
        wiki()
        getRow()
    elif tone_row.lower() == "info":
        info()
        getRow()
    else:
        tone_row = tone_row.split()


    for n, i in enumerate(tone_row): ### Try checks for integers, Except allows user to enter T and E for 10 and 11.
        try:
            value = int(i)
            tone_row[n] = value
        except ValueError:
            if i.lower() == "t":
                tone_row[n] = 10
            elif i.lower() == "e":
                tone_row[n] = 11
            else:
                print("\n\nError: Please enter numbers, t, or e only.\n\n")
                getRow()


    for i in tone_row: ### Checks about repeated numbers
        if tone_row.count(i) > 1:
            print("\n\nAre you sure you'd like repeating numbers? (y/n)")
            inp = input().lower()
            if inp == "n":
                print("\n")
                getRow()
            elif inp == "re":
                print("\n")
                getRow()
            elif inp == "wiki":
                wiki()
            elif inp == "info":
                info()
                getRow()
            break

    
    if len(tone_row) != 12: ### Non-Standard row length
        print("\n\nYou've entered a row of length ", len(tone_row), ".")
        print("Did you mean to enter a row without 12 notes? (y/n)")
        inp = input().lower()
        if inp == "n":
            print("\n")
            getRow()
        elif inp == "re":
            print("\n")
            getRow()
        elif inp == "wiki":
            wiki()
        elif inp == "info":
            info()
            getRow()
    

    
    def zeroFirst(row): ### First row at 0
        x = row[0]
        for n, i in enumerate(row):
            row[n] = (i + (12 - x)) % 12
        return row
    


    if tone_row[0] % 12 != 0: ### Checks if starts at 0
        print("\n\nWould you like your prime row to start at 0? (y/n)")
        inp = input().lower()
        if inp.lower() == "y":
            tone_row = zeroFirst(tone_row)
        elif inp == "re":
            print("\n")
            getRow()
        elif inp == "wiki":
            wiki()
        elif inp == "info":
            info()
            getRow()
    
        

    def generateMatrix(generating_row):
        print("\n\n\nYour Matrix:\n\n")
        index_one = tone_row[0]
        x = 0
        while x < len(generating_row): ### Generates a Matrix from the row
            row = [((index_one-tone_row[x])+i)%12 for i in generating_row]
            matrix.append(row)
            x += 1

        
        for row in matrix: ### Converts 10/11 to T/E
            double_digits = {'10': 'T', '11': 'E'}
            row = ' '.join(map(str, row))
            for key in double_digits:
                row = str.replace(row, key, double_digits[key])
            print(row)

    

    matrix = generateMatrix(tone_row)

    print("\n\n")
    
    
    
    def leave(): ### For quitting
        print("Enter to Quit")
        inp = input().lower()
        if inp == "wiki":
            wiki()
            again()
        elif inp == "info":
            info()
            again()
        elif inp == "re":
            getRow()
        else:
            exit()


    
    def again(): ### For starting over
        print("\nNew Matrix? (y/n)")
        inp = str(input()).lower()
        if inp == "y":
            print("")
            getRow()
        elif inp == "n":
            print("\n")
            leave()
        elif inp == "wiki":
            wiki()
            again()
        elif inp == "info":
            info()
            again()
        else:
            again()


    
    again()

    
getRow()

