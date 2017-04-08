# NIST-SD4 Dataset

## About the Dataset

The NIST-SD4 is a freely available fingerprint collection, compiled and curated by the [NIST](https://www.nist.gov/) *(National Institute of Standards and Technology)*. It contains 2000 8-bit gray scale fingerprint image pairs. Each image is 512-by-512 pixels with 32 rows of white space at the bottom and classified using one of the five following classes:

+ Arch (A)
+ Left Loop (L)
+ Right Loop (R)
+ Tented Arch (T)
+ Whorl (W)

The database is evenly distributed over each of the five classifications with 400 fingerprint pairs from each class.

The text file that accompanies each image gives the Gender, Class and History information extracted from the ANSI/NIST-ITL formatted (AN2) file.

NIST Special Database 4 has the following features:

+ 2000 8-bit gray scale fingerprint image pairs including classifications
+ 400 fingerprint pairs from each of the five classifications - Arch, Left and Right Loops, Tented Arch, Whirl)
+ each of the fingerprint pairs are two completely different rollings of the same fingerprint
+ 19.7 pixels per millimeter resolution
+ Suitable for automated fingerprint classification research, the database can be used for algorithm development and system training and testing.

## Transformations

The default file layout and names in the dataset is not very convenient for the training and testing processes that will be done as part of this experiment. The following transformations will be done to the files:

+ All files are distributed in two folders: Test and Train.
    + Test files is a subset of 500 images (250 pairs), corresponding to the *figs_0* folder of the original data set.
    + The remaining 1750 pairs of images - corresponding to the *figs_1* to *figs_7* folders - are localted in the Train folder.
+ All text files have been removed.
+ Naming convention of file names has changed to **XXXX_O_FF_G_C.png**, with the following placeholders:
    + XXXX: Identifier of the individual
    + 0: Order
    + FF: Finger number
    + G: Gender, with possible values F and M
    + C: Fingerprint Class

### Code Dictionaries for naming conventions:

**Codes for Order of fingerprint**

|Code | Description |
|:--- |:-----------:|
|F    |First        |
|S    |Second       |

**Codes for Gender**

|Code | Description |
|:--- |:-----------:|
|M    |Male         |
|F    |Female       |

**Codes for Finger numbers**^

|Number | Finger       |
|:----- |:------------:|
|01     |Right Thumb   |
|02     |Right Index   |
|03     |Right Middle  |
|04     |Right Ring    |
|05     |Right Little  |
|06     |Left Thumb    |
|07     |Left Index    |
|08     |Left Middle   |
|09     |Left Ring     |
|10     |Left Little   |

**Codes for Fingerprint class:**

| Class | Description |
| ------|:-----------:|
| A     |Arch         |
| L     |Left Loop    |
| R     |Right Loop   |
| T     |Tented Arch  |
| W     |Whorl        |

## Usage Instructions

The dataset is not distributed with the figerprint classification model, although it can be downloaded manually from the [NIST-SD4 page](https://www.nist.gov/srd/nist-special-database-4). It can also be downloaded automatically running the following Python command from the DataSets/NIST-SD4 directory:

`python setup_dataset.py`
