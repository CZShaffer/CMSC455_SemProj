import json
import os
# import time

def formatLine(line, params):
    newTokens = {}  # dict to hold specified parameters and their values

    # load the line into JSON object
    line_object = json.loads(line)

    # for each of the specified parameters, appends both the field and its
    # value if they exist, otherwise returns empty dict
    for field in params:
        if field not in line_object or line_object[field] == None:
            return {}
        newTokens[field] = line_object[field]

    # changes dict to JSON object
    json_str = json.dumps(newTokens)

    return json_str


def main():
    filename = "D:\\CMSC 455\\Test\\30.json"
    writeFile = "D:\\CMSC 455\\Cleaned\\cleanedTweets.json"

    file = open(filename, "r")
    outfile = open(writeFile,"w")

    params = ["created_at", "text", "place", "lang"]  # parameters to grab from tweets

    # takes each line from the json file, removes unneeded data, then writes to output
    for line in file:
        newline = formatLine(line, params)

        if bool(newline) is True:
            outfile.write(newline)
            outfile.write("\n")

    file.close()
    outfile.close()

# start_time = time.time()
main()
# print("--- %s seconds ---" % (time.time() - start_time))