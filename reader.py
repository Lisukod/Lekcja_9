from sys import argv
import csv

src = argv[1]
dst = argv[2]


with open("csv_origin/{}".format(src), "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("edited/{}".format(dst), "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter=",")

        for line in csv_reader:
            csv_writer.writerow(line)