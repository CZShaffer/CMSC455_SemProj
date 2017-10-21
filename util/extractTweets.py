import os
import bz2

# Will combine these to for loops into their own separate functions later.

def main():

    originalData = "D:\\CMSC 455\\Original Data\\"
    compressedData = "D:\\CMSC 455\\Compressed_Tweets\\"
    outputFileName = os.path.join("D:\\CMSC 455\\Uncompressed Tweets\\", "tweets.json")
    outputFile = open(outputFileName, "a+")

    i = 0

    tweetNumber = 0

    # Go through directories in workingDirectory.
    for root, directories, files in os.walk(originalData):

        # Go through the files.
        for file in files:

            # Rename the files.
            os.rename(os.path.join(root, file), os.path.join("D:\\CMSC 455\\Compressed_Tweets\\", str(i) + ".json.bz2"))

            i += 1

    # Uncompress each bz2 file and add it to a single file.
    for root, directories, files in os.walk(compressedData):

        for file in files:

            uncompressedData = bz2.BZ2File(os.path.join(compressedData, file), "r")

            for line in uncompressedData:

                tweetNumber += 1

                #print(line.decode(encoding='UTF-8').strip())
                outputFile.write(line.decode(encoding='UTF-8').strip() + "\n")
                #print(tweetNumber)

            uncompressedData.close()

main()