import json
import math
filename = "en_tweets.json"
outputdir = "csv_files_split/"

header = "latitude,longitude,neg,neu,pos,compound\n"
dict = open(filename,"r")
hourDict = {}
for line in dict:
    data = json.loads(line)
    for country in data:
        for hour in data[country]:
            if hour not in hourDict:
                hourDict[hour] = []
            for tweetData in data[country][hour]:
                hourDict[hour].append(tweetData)

for hour in hourDict:
    posfilename = outputdir + str(hour) + "_pos.csv"
    posfile = open(posfilename, "w")
    negfilename = outputdir + str(hour) + "_neg.csv"
    negfile = open(negfilename, "w")
    neufilename = outputdir + str(hour) + "_neu.csv"
    neufile = open(neufilename, "w")
    for pair in hourDict[hour]:
        sentimentDict = json.dumps(pair[0])
        sentiment = json.loads(sentimentDict)
        latitude = pair[1][1]
        longitude = pair[1][0]
        if sentiment["compound"] <= -0.5:
            negfile.write("%f,%f,%f,%f,%f,%f\n" % (latitude,longitude,sentiment["neg"],sentiment["neu"],sentiment["pos"],-1*sentiment["compound"]))
        elif sentiment["compound"] >= 0.5:
            posfile.write("%f,%f,%f,%f,%f,%f\n" % (latitude,longitude,sentiment["neg"],sentiment["neu"],sentiment["pos"],sentiment["compound"]))
        else:
            neufile.write("%f,%f,%f,%f,%f,%f\n" % (latitude,longitude,sentiment["neg"],sentiment["neu"],sentiment["pos"],1 - math.fabs(sentiment["compound"])))
