#python2
#put this code and the txt file in the same folder
#convert semicolon txt file into comma separated file
fname = raw_input("Enter the file name: ")
fcsv = raw_input("Enter the new file name: ")
f2 = open(fcsv, 'a') # create a new output.txt file in the same directory

try:
    fhand = open(fname)
except:
    print "Cannot find the file. Check file name"
    exit()

# read lines in the files
for line in fhand:
    ## line = line.rstrip().upper() # take out the \n at the end of each line and upper case
    line = line.replace(';', ',') # replace ";" with ",", can be applied for other formats of replacement
    f2.write(line) # save to a new file
    ##print line_upper
fhand.close()
f2.close()
