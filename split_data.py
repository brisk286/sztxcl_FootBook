import os
import random
import shutil

if __name__ == '__main__':
    allData = r"C:\"
    trainData = r"C:\"
    testData = r"C:\"

    files = os.listdir(allData)
    numData = len(files)

    testFiles = random.sample(files, int(numData / 5))

    for file in files:
        if file in testFiles:
            shutil.copyfile(allData + "\\" + file, testData + "\\" + file)
        else:
            shutil.copyfile(allData + "\\" + file, trainData + "\\" + file)
