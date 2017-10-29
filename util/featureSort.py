import json

def featureSort(items,param):
    sortedDict = {}
    # converts each line from json object to string, and sorts them into a dictionary by the specified parameter
    for item in items:
        line = json.loads(item)
        # sorts each tweet by values of the passed in parameter
        if line[param] not in sortedDict:
            sortedDict[line[param]] = []
        sortedDict[line[param]].append(json.dumps(line))

    return sortedDict

def filter(items,param,values):
    featureDict = featureSort(items,param)
    filterList = []
    # adds all tweets with one of the given values for param into a single list
    for value in values:
        if value in featureDict:
            filterList += featureDict[value]

    return filterList

def multiFilter(items,paramAndVal):
    retList = items
    # successively filters out values by each parameter
    for pair in paramAndVal:
        retList = filter(retList, pair[0], pair[1])

    return retList

def main():
    filename = "cleaned.json"
    writeFile = "output.json"
    file = open(filename, "r")
    outfile = open(writeFile, "w")
    # searchPV is the parameters and values to filter by. Expected to be of the format
    # [(param1, [value11,value12,...,value1n]), (param2, [value21, value22,...,value2n]),...,(paramn, [valuen1, valuen2,..., valuenn])]
    searchPV = [("lang",["en","ja"]),("created_at",["Sat May 06 06:33:58 +0000 2017","Sat May 06 06:33:59 +0000 2017"])]

    outDict = multiFilter(file, searchPV)

    for item in outDict:
        outfile.write(item)
        outfile.write("\n")

    file.close()
    outfile.close()

main()
