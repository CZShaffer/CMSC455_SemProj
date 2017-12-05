import json

def saveDict(dictionaryOfSents, fileToSaveTo):

    with open(fileToSaveTo, "w") as output:

        json.dump(dictionaryOfSents, output)

def main():

    fileName = "dictFile.json"

    file = open(fileName, "r")

    dictOfAverageSentiments = {}
    dictOfSentiments = json.load(file)

    for region in dictOfSentiments:

        dictOfAverageSentiments[region] = {}

        for hour in range(0, 24):

            stringHour = ""

            if hour < 10:

                stringHour = "0" + str(hour)

            else:

                stringHour = str(hour)

            tweets = 0

            if stringHour not in dictOfSentiments[region]:

                dictOfAverageSentiments[region][stringHour] = 0

                print("No tweets during " + str(hour) + " for " + str(region))

            else:

                dictOfAverageSentiments[region][stringHour] = 0

                for tweet in dictOfSentiments[region][stringHour]:

                    tweets += 1

                    dictOfAverageSentiments[region][stringHour] += tweet[0]["compound"]

                dictOfAverageSentiments[region][stringHour] /= tweets

                print("The average sentiment for the " + str(region) + " during " + stringHour + " is " + str(dictOfAverageSentiments[region][stringHour]))

    saveDict(dictOfAverageSentiments, "dictOfAverageSentimentsFinalFinal.json")

main()