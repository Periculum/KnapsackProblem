# Rucksackproblem (rekursiv gelöst)
volume = 100
pieces = 30
rucksack = []
valuePerPiece = []


# Datei mit Testwerten einlesen in ein zweidimensionales Array vom Typ [volume][wert]
def getList():
    with open("rucksack.txt") as file:
        for number in file:
            rucksack.append(number.strip().split(' '))


# rekursive Methode
def rekursiv(i, currentvolume):
    if (i < 0):
        return 0
    if (int(rucksack[i][0]) > currentvolume):
        return rekursiv(i - 1, currentvolume)
    else:
        tmp = rekursiv(i - 1, currentvolume -
                       int(rucksack[i][0])) + int(rucksack[i][1])
        return max(rekursiv(i - 1, currentvolume), tmp)


def main():
    getList()
    print(rucksack)
    print(rekursiv(pieces - 1, volume))


if __name__ == "__main__":
    main()
