import json
import pandas as pd

def saveDict(dictionaryOfSents, fileToSaveTo):

	with open(fileToSaveTo, "w") as output:

		json.dump(dictionaryOfSents, output)

def main():

	fileName = "dictOfAverageSentimentsFinalFinal.json"

	file = open(fileName, "r")

	dictOfAverageSentiments = json.load(file)

	dictOfCountriesWith24Hrs = {}

	for region in dictOfAverageSentiments:

		numHours = 0

		for hour in dictOfAverageSentiments[region]:

			if dictOfAverageSentiments[region][hour] != 0:

				numHours += 1

		if numHours == 24:

			print(region + " has 24 hours!")

			dictOfCountriesWith24Hrs[region] = {}

			for realHour in range(0, 24):

				stringHour = ""

				if realHour < 10:

					stringHour = "0" + str(realHour)

				else:

					stringHour = str(realHour)

				dictOfCountriesWith24Hrs[region][realHour] = dictOfAverageSentiments[region][stringHour]

			print(region +  " has 24 hours")

	for region in dictOfCountriesWith24Hrs:

		df = pd.DataFrame(data = dictOfCountriesWith24Hrs[region], index=[0])
		df = (df.T)
		df.to_excel(str(region) + "averages.xlsx")

main()