import csv
fOpen = raw_input("Enter csv file name: ")
fOutput = raw_input("Enter csv file name with added column: ")
with open(fOpen,'r') as csvinput:
    with open(fOutput, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('Berry')
        all.append(row)

        for row in reader:
            row.append(row[0])
            all.append(row)

        writer.writerows(all)
