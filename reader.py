from sys import argv
from os import listdir
from os.path import exists, isfile, join
import csv

src = argv[1]
dst = argv[2]
changeList = []
csvList = []

if not exists("./csv_origin/{}".format(src)):
    print("Błąd. Podana ścieżka nie istnieje")
    exit()
elif not isfile("./csv_origin/{}".format(src)):
    print("Błąd. Podana ścieżka nie jest plikiem.")
    onlyfiles = [
        f for f in listdir("./csv_origin/") if isfile(join("./csv_origin/", f))
    ]
    print("Pliki w katalogu:\n{}".format(onlyfiles))
    exit()


with open("csv_origin/{}".format(src), "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("edited/{}".format(dst), "w") as new_file:
        csv_writer = csv.writer(new_file)

        for line in csv_reader:
            csvList.append(line)

        for change in argv[3:]:
            change = change.split(",")
            Y = int(change[0])
            X = int(change[1])
            value = change[2]
            csvList[Y][X] = value

        for line in csvList:
            csv_writer.writerow(line)
