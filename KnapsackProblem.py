# Rucksackproblem
volume = 100
pieces = 30
rucksack = []
valuePerPiece = []


# Datei mit Testwerten einlesen in ein zweidimensionales Array vom Typ [volume][wert]
def getList():
    with open("rucksack.txt") as file:
        for number in file:
            rucksack.append(number.strip().split(' '))


# Wert pro Volume feststellen und in einem anderen Array abspeichern
def ratePieces():
    for i in range(pieces):
        valuePerPiece.append((int(rucksack[i][1]) / int(rucksack[i][0])))


# Werte sortieren
def sortPieces():
    tmp = 0
    for i in range(pieces):
        max_index = i
        for j in range(i + 1, pieces):
            if valuePerPiece[j] > valuePerPiece[max_index]:
                max_index = j
            elif(valuePerPiece[j] == valuePerPiece[max_index] and rucksack[j][0] > rucksack[max_index][0]):
                max_index = j
        # Werte tauschen in ValuePerPiece
        valuePerPiece[i], valuePerPiece[max_index] = valuePerPiece[max_index], valuePerPiece[i]
        # Werte tauschen in rucksack
        rucksack[i], rucksack[max_index] = rucksack[max_index], rucksack[i]


# Schauen, welche der Teile in den Rucksack passen
def choosePieces():
    currentVolume = 0
    total = 0
    articles = []
    for i in range(pieces):
        if((currentVolume + int(rucksack[i][0])) <= volume):
            currentVolume += int(rucksack[i][0])
            total += int(rucksack[i][1])
            articles.append(rucksack[i])

    print("Folgende Produkte mit einem Gesamtgewicht von " + str(currentVolume) + " können mitgenommen werden: " +
          str(articles) + " mit einem Gesamtwert von " + str(total))


def main():
    getList()
    ratePieces()
    sortPieces()
    choosePieces()


if __name__ == "__main__":
    main()
