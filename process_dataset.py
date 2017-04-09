# Import the relevant modules to be used later
import gzip
import numpy as np
import os
import glob
import shutil
import struct
import sys
from scipy.misc import imread

def encodeFingerprintClassFromFileName(fileName):
    """Converts the fingerprintType into the one-hot encoding format."""
    fileName = os.path.basename(fileName)
    fingerprintClass = fileName[12]
    
    if fingerprintClass.upper() == "A":
        return np.array([1, 0, 0, 0, 0])
    elif fingerprintClass.upper() == "L":
        return np.array([0, 1, 0, 0, 0])
    elif fingerprintClass.upper() == "R":
        return np.array([0, 0, 1, 0, 0])
    elif fingerprintClass.upper() == "T":
        return np.array([0, 0, 0, 1, 0])
    elif fingerprintClass.upper() == "W":
        return np.array([0, 0, 0, 0, 1])

def imagesToVector(sourceFolder, imagesToProcess = 0):
    """Converts the PNG images to a one-dimensional vector, with an initial one-hot encodding for the feature"""

    # Iterate all the images allowed by the imagesToProcess parameter
    files = glob.glob(os.path.join(sourceFolder, "*.png"))
    imgCont = 1
    if imagesToProcess == 0:
        numRows = len(files)
    else:
        numRows = min(len(files),imagesToProcess)
    numFeatures = 5
    res = np.ndarray(shape = (numRows, 512*512 + numFeatures), dtype = np.uint8)

    for file in files:

        if imgCont > imagesToProcess:
            break

        # Extract the features
        features = encodeFingerprintClassFromFileName(file)

        # Extract the bytes of the 512 x 512 images as a vector
        img = imread(file, flatten = True)
        flattened = img.ravel()
        res[imgCont-1] = np.concatenate([features,flattened])
        
        imgCont += 1

    return res


def saveToTxt(filename, vector):
    """Saves the image vectors to One-Hot encoding text files, compatible with the CNTK text reader"""

    print("Saving file: ", filename)
    with open(filename, "w") as f:
        # labels = list(map(' '.join, np.eye(10, dtype=np.uint).astype(str)))
        for row in vector:
            label_str = ' '.join(row.astype(str)[0:5])
            feature_str = ' '.join(row.astype(str)[5:])
            f.write("|labels {} |features {}\n".format(label_str, feature_str))

def processImages(sourceFolder, outputFileName, imagesToProcess = 0):
    images = imagesToVector(sourceFolder, imagesToProcess)
    saveToTxt(outputFileName, images)

if __name__ == "__main__":
    trainFolder = os.path.join("DataSets", "NIST-SD4", "train")
    testFolder = os.path.join("DataSets", "NIST-SD4", "test")

    processImages(trainFolder, os.path.join(trainFolder, "trainData.txt"))
    processImages(testFolder, os.path.join(testFolder, "testData.txt"))