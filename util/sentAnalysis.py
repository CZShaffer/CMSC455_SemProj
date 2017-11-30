import json
from googletrans import Translator
import os
from vaderSentiment import vaderSentiment
import re
import emoji

def saveDict(dictionaryOfSents, fileToSaveTo):

    with open(fileToSaveTo, "w") as output:

        json.dump(dictionaryOfSents, output)

def getLanguages(languageFileName):

    languages = {}

    file = open(languageFileName, "r")
    for line in file:
        cleanedLine = (line.strip()).split()
        languages[cleanedLine[1]] = cleanedLine[0]

    return languages

def cleanTweets(fileName, outputFileName):

    inputFile = open(fileName, "r")
    outputFile = open(outputFileName, "a+")

    for line in inputFile:

        tweet = json.loads(line)

        if tweet["lang"] != "und":

            tweet["text"] = tweet["text"].replace("\n", ".")

            print(tweet["text"])

            outputFile.write(json.dumps(tweet))
            outputFile.write("\n")

def main():

    emojiPattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U0001F100-\U0001F1FF"
                               u"\U0001F780-\U0001F999"
                               u"\u2000-\u206F"
                               u"\u2701-\u27BF"
                               "]+", flags=re.UNICODE)

    fileName = "cleanedTweets.json"

    outputFileName = "finalTweets.json"

    file = open(fileName, "r")

    languages = getLanguages("Languages.txt")
    print(languages)

    #cleanTweets(fileName, outputFileName)

    translator = Translator()

    #with open("dictFile.json") as jsonData:

    #regionsToSentiments = json.load(jsonData)

    #regionsToSentiments = json.loads(file)

    regionsToSentiments = {}

    workingPath = "C:\\Users\\Taylor\\Desktop\\TEST\\Countries"

    analyzer = vaderSentiment.SentimentIntensityAnalyzer()

    usa = "US_EN.json"

    #for root, directories, files in os.walk(workingPath):

        #for file in files:

    tweet = 0

    realFile = open(usa, "r")

    for line in realFile:

        #print(file)
        tweet += 1
        print(tweet)

        tweetObject = json.loads(line)
        # print(tweetObject)

        originalTweet = tweetObject["text"]
        #originalTweet = emojiPattern.sub(r'', originalTweet)
        # print(originalTweet)
        # originalTweet = ''.join(character for character in tweetObject["text"] if character not in emoji.UNICODE_EMOJI)

        '''
        if tweetObject["lang"] != "en":

            # print("Original Tweet:" + str(tweetObject["text"]))
            # print(tweetObject["lang"])

            if tweetObject["lang"] in languages:

                # Translates the tweet from its native language to English.
                translatedTweet = translator.translate(originalTweet, dest="en", src=tweetObject["lang"]).text
                # print("Translated Tweet: " + str(translatedTweet))

            else:

                transObject = translator.translate(originalTweet, dest="en")
                translatedTweet = transObject.text
                # print("Translated Tweet: " + str(translatedTweet))

        else:

            translatedTweet = tweetObject["text"]
        '''

        sentiment = analyzer.polarity_scores(originalTweet)
        coordinates = (tweetObject["place"]["bounding_box"]["coordinates"][0][0][0],
                       tweetObject["place"]["bounding_box"]["coordinates"][0][0][1])
        # print(sentiment)
        # print(coordinates)

        if tweetObject["place"]["country_code"] not in regionsToSentiments:

            regionsToSentiments[tweetObject["place"]["country_code"]] = {}

            if tweetObject["created_at"].split()[3][0:2] not in regionsToSentiments[
                tweetObject["place"]["country_code"]]:
                regionsToSentiments[tweetObject["place"]["country_code"]][tweetObject["created_at"].split()[3][0:2]] = [
                    (sentiment, coordinates)]

            else:

                regionsToSentiments[tweetObject["place"]["country_code"]][
                    tweetObject["created_at"].split()[3][0:2]].append((sentiment, coordinates))

        else:

            if tweetObject["created_at"].split()[3][0:2] not in regionsToSentiments[
                tweetObject["place"]["country_code"]]:
                regionsToSentiments[tweetObject["place"]["country_code"]][tweetObject["created_at"].split()[3][0:2]] = [
                    (sentiment, coordinates)]

            else:

                regionsToSentiments[tweetObject["place"]["country_code"]][
                    tweetObject["created_at"].split()[3][0:2]].append((sentiment, coordinates))

        print()

    print(regionsToSentiments)

    saveDict(regionsToSentiments, "dictFile.json")

main()