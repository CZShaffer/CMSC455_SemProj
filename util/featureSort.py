import json

def featureSort(items,param):
    sortedDict = {}
    # converts each line from json object to string, and sorts them into a dictionary by the specified parameter
    for item in items:
        line = json.loads(item)
        # sorts each tweet by values of the passed in parameter
        if param not in line:
            return {}
        if line[param] not in sortedDict:
            sortedDict[line[param]] = []
        sortedDict[line[param]].append(json.dumps(line))

    return sortedDict

def deepSort(items,param,deepParam):
    sortedDict = {}
    # converts each line from json object to string, and sorts them into a dictionary by the specified parameter
    print("sorting")
    for item in items:
        line = json.loads(item)
        # sorts each tweet by values of the passed in parameter
        if param not in line:
            return {}
        if line[param] is not None:
            deepJson = json.dumps(line[param])
            deepLine = json.loads(deepJson)
            print(deepLine)
            if deepLine[deepParam] not in sortedDict:
                sortedDict[deepLine[deepParam]] = []
            sortedDict[deepLine[deepParam]].append(json.dumps(line))

    return sortedDict

def filter(items,param,values):
    featureDict = featureSort(items,param)
    filterList = []
    # adds all tweets with one of the given values for param into a single list
    for value in values:
        if value in featureDict:
            filterList += featureDict[value]

    return filterList

def deepFilter(items,param,deepParam,values):
    featureDict = deepSort(items,param,deepParam)
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
        if len(pair) is 2:
            retList = filter(retList, pair[0], pair[1])
        else:
            retList = deepFilter(retList, pair[0], pair[1], pair[2])

    return retList

def main():
    filename = "cleanedTweets.json"
    writeFile = "output.json"
    file = open(filename, "r")
    outfile = open(writeFile, "w")
    # searchPV is the parameters and values to filter by. Expected to be of the format:
    # [(param1, [value11,value12,...,value1n]), (param2, [value21, value22,...,value2n]),...,(paramn, [valuen1, valuen2,..., valuenn])]
    # in cases where the parameter contains a json object, the tuple should be of the form:
    # (param1, deepParam1, [value11,value12,...,value1n])
    searchPV = [("lang",["en","ja"]),("place","country_code",["US", "JP"])]

    outDict = multiFilter(file, searchPV)

    for item in outDict:
        outfile.write(item)
        outfile.write("\n")

    file.close()
    outfile.close()

main()
