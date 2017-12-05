import json
import math
filename = "en_tweets.json"
outputdir = "csv_files_split/"

# def featureSort(items,param):
#     sortedDict = {}
#     # converts each line from json object to string, and sorts them into a dictionary by the specified parameter
#     for item in items:
#         line = json.loads(item)
#         # sorts each tweet by values of the passed in parameter
#         if param not in line:
#             return {}
#         if line[param] not in sortedDict:
#             sortedDict[line[param]] = []
#         sortedDict[line[param]].append(json.dumps(line))
#
#     return sortedDict

# country: -> hour: ->[[{sentiment},[coordinates]]]
# country: json obj, hour: json obj, sentiment: json obj, coordinates: float[]
header = "latitude,longitude,neg,neu,pos,compound\n"
# outfile = open(outputdir,"w")
dict = open(filename,"r")
# outfile.write(header)
hourDict = {}
for line in dict:
    data = json.loads(line)
    # print(data)
    for country in data:
        # print(country)
        # print(data[country])
        # hourData = json.loads(data[country])
        for hour in data[country]:
            # print(hour)
            # print(data[country][hour])
            if hour not in hourDict:
                hourDict[hour] = []
            for tweetData in data[country][hour]:
                hourDict[hour].append(tweetData)
            # for pair in data[country][hour]:
            #     # print(pair)
            #     # for item in pair:
            #     #     print(item)
            #     sentimentDict = json.dumps(pair[0])
            #     sentiment = json.loads(sentimentDict)
            #     # print(sentiment)
            #     # print(pair[1])
            #     # for item in sentiment:
            #     #     print(sentiment[item])
            #     latitude = pair[1][0]
            #     longitude = pair[1][1]
            #     # print(latitude)
            #     # print(longitude)
            #     outfile.write("%f,%f,%f,%f,%f,%f\n" % (latitude,longitude,sentiment["neg"],sentiment["neu"],sentiment["pos"],sentiment["compound"]))
for hour in hourDict:
    # print(hour)
    posfilename = outputdir + str(hour) + "_pos.csv"
    posfile = open(posfilename, "w")
    negfilename = outputdir + str(hour) + "_neg.csv"
    negfile = open(negfilename, "w")
    neufilename = outputdir + str(hour) + "_neu.csv"
    neufile = open(neufilename, "w")
    for pair in hourDict[hour]:
        # print(pair)
        # for item in pair:
        #     print(item)
        sentimentDict = json.dumps(pair[0])
        sentiment = json.loads(sentimentDict)
        # print(sentiment)
        # print(pair[1])
        # for item in sentiment:
        #     print(sentiment[item])
        latitude = pair[1][1]
        longitude = pair[1][0]
        # print(latitude)
        # print(longitude)
        if sentiment["compound"] <= -0.5:
            negfile.write("%f,%f,%f,%f,%f,%f\n" % (latitude,longitude,sentiment["neg"],sentiment["neu"],sentiment["pos"],-1*sentiment["compound"]))
        elif sentiment["compound"] >= 0.5:
            posfile.write("%f,%f,%f,%f,%f,%f\n" % (latitude,longitude,sentiment["neg"],sentiment["neu"],sentiment["pos"],sentiment["compound"]))
        else:
            neufile.write("%f,%f,%f,%f,%f,%f\n" % (latitude,longitude,sentiment["neg"],sentiment["neu"],sentiment["pos"],1 - math.fabs(sentiment["compound"])))
