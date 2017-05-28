import csv
import sys
import operator
import collections

def getPos(array, string):
    try:
        val = array.index(string)
    except:
        val = -10000000000
    return val


def checkMultiString(olddict, newdict, mystr, val, inputArray):
    deleted =[]
    for key in newdict:
        pos = getPos(newdict[key], mystr)
        if(pos>=0):
            deleted.append(mystr)
            x = newdict[key]
            del x[pos]
            origval = val
            checkVal = val
            for inputstr in inputArray:
                for string in x:
                    if string == inputstr:
                        checkVal += checkSingleString(olddict, string)
                        del x[x.index(string)]
                        deleted.append(string)

            for inputArrays in inputArray:
                for deletedString in deleted:
                    if inputArrays == deletedString:
                        del inputArray[inputArray.index(deletedString)]
            if (checkVal > float(key)):
                val = float(key)
                return val
            else:
                return val
    return val

def checkSingleString(olddict, mystr):
    val=float('inf')
    if mystr in olddict:
        val = float(olddict[mystr])
    return val

ifile = open(sys.argv[1], "rb")
rownum = 0
olddict = {}
newdict ={}
reader = csv.reader(ifile)

for rows in reader:
    if(len(rows) == 3):
        x = rows[2].replace(" ", "")
        if x in olddict:
            if (float(olddict[x]) < float(rows[1])):
                continue
        olddict[x] = rows[1]
    else:
        rowdupe =[]
        for row in rows[2:]:
            rowdupe.append(row.replace(" ",""))
        newdict[float(rows[1].replace(" ", ""))] = rowdupe

d = collections.OrderedDict(sorted(newdict.items()))
newdict = d
inputArray = sys.argv[2:]
sum1 = 0
for string in inputArray:
    sum1 += checkMultiString(olddict, newdict, string, checkSingleString(olddict, string), inputArray)

if sum1>10000000000:
    print "Cost Efficient Solution not possible"
else:
    print "Most Cost Efficient Solution: ", sum1
ifile.close()
