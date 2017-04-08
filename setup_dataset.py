"""This module downloads and distributes the NIST_SD4 dataset."""

import zipfile
import os
import glob
import shutil

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

class Fingerprint:
    """Holds the metadata of each fingerprint sample"""

    def __init__(self, identifier, order, finger, gender, fingerprintClass):
        self.id = identifier
        self.order = order
        self.finger = finger
        self.gender = gender
        self.fingerprintClass = fingerprintClass

    def __repr__(self):
        return "ID: " + str(self.id) + " ORDER: " + str(self.order) + " FINGER: " + str(self.finger) + " GENDER: " + str(self.gender) + " CLASS: " + str(self.fingerprintClass)
    def __str__(self):
        return "ID: " + str(self.id) + " ORDER: " + str(self.order) + " FINGER: " + str(self.finger) + " GENDER: " + str(self.gender) + " CLASS: " + str(self.fingerprintClass)


def downloadDataset(datasetName, url):
    """Downloads the dataset if needed, and copies the files to the appropiate directories."""

    baseFolder = os.path.dirname(os.path.abspath(__file__))
    destinationFolder = os.path.join(baseFolder, "DataSets", datasetName)
    testFolder = os.path.join(destinationFolder, "test")
    trainFolder = os.path.join(destinationFolder, "train")

    if not os.path.exists(os.path.join(destinationFolder, "test")):
        filename = os.path.join(destinationFolder, "NISTSpecialDatabase4GrayScaleImagesofFIGS.zip")
        if not os.path.exists(filename):
            print("Downloading data from " + url + "...")
            urlretrieve(url, filename)

        try:
            print("Extracting " + filename + "...")
            with zipfile.ZipFile(filename) as myzip:
                myzip.extractall(destinationFolder)
            print("Distributing the Dataset...")
            distributeDataset(destinationFolder, testFolder, trainFolder)
            print("Renaming the files...")
            renameFiles(testFolder)
            renameFiles(trainFolder)
        finally:
            os.remove(filename)
        print("Done.")
    else:
        print("Data already available at " + baseFolder + "/" + datasetName)

def distributeDataset(destinationFolder, testFolder, trainFolder):
    """Creates the Test and Train directories if needed, and moves the images into them."""
    
    # Set up directories for test and training data sets
    if not os.path.exists(testFolder):
        os.makedirs(testFolder)
    if not os.path.exists(trainFolder):
        os.makedirs(trainFolder)

    # Generate list of directories
    dirs = []
    for i in range(0,8):
        dirs.append(os.path.join(destinationFolder, "NISTSpecialDatabase4GrayScaleImagesofFIGS\\sd04\\png_txt\\figs_" + str(i)))

    # Extract Test data
    files = os.listdir(dirs[0])

    for filename in files:
        shutil.copy(os.path.join(dirs[0], filename), testFolder)
    shutil.rmtree(dirs[0])

    # Extract Train data
    for i in range(1,8):

        files = os.listdir(dirs[i])
        for filename in files:
            shutil.copy(os.path.join(dirs[i], filename), trainFolder)
        shutil.rmtree(dirs[i])
    shutil.rmtree(os.path.join(destinationFolder, "NISTSpecialDatabase4GrayScaleImagesofFIGS"))

def renameFiles(folder):
    """Renames all files so the names hold the metadata information."""

    # Retrieve list of all text files and remove the txt files
    for filename in glob.glob(os.path.join(folder, "*.txt")):
        with open(filename, 'r') as file:
            metadata=file.read().replace('\n', '')
        ident = metadata[27:31]
        order = metadata[26].upper()
        finger = metadata[32:34]
        gender = metadata[8].upper()
        fingerprintClass = metadata[16].upper()
        fp = Fingerprint(ident, order, finger, gender, fingerprintClass)

        # Remove the .txt file and rename the png
        os.remove(filename)
        pngName = filename.replace(".txt", ".png")
        newName = fp.id + "_" + fp.order + "_" + fp.finger + "_" + fp.gender + "_" + fp.fingerprintClass + ".png"
        newName = os.path.join(folder, newName)
        os.rename(pngName, newName)

if __name__ == "__main__":
    datasetName = "NIST-SD4"
    url = "https://s3.amazonaws.com/nist-srd/SD4/NISTSpecialDatabase4GrayScaleImagesofFIGS.zip"

    downloadDataset(datasetName, url)
