# Fingerprint Classification

This project implements a fingerprint classificator using an auto-encoder model, implemented via Microsoft's CNTK. 

This is initial stage of the fingerprint matching system, in which the fingerprint is classified according to the specific type. These types can be of one of the following classes:

+ Arch (A)
+ Left Loop (L)
+ Right Loop (R)
+ Tented Arch (T)
+ Whorl (W)

Once the fingerprint has been classified, it will be passed to the actual matching stage *(minutia matching)*, which is implemented in a sepparate model.

## Solution Components


## Persons of Interest

The stakeholders are:

* Pablo Alvarez Doval (<palvarez@plainconcepts.com>)