import json
import os
# import time

def formatLine(line, params):
    newTokens = {}

    line_object = json.loads(line)

    for field in params:

        if field not in line_object or line_object[field] == None:
            return {}

        newTokens[field] = line_object[field]

    json_str = json.dumps(newTokens)

    return json_str

def main():

    filename = "D:\\CMSC 455\\Test\\30.json"
    writeFile = "D:\\CMSC 455\\Cleaned\\cleanedTweets.json"

    file = open(filename, "r")
    outfile = open(writeFile,"w")

    params = ["created_at", "text", "place", "lang"]

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