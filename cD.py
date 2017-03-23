#!/usr/bin/env python
#coding:utf-8
import difflib
dirNames=[]
fileNames = []
numberofFiles = 0
previousName = ''
readData = 'books.txt'

def checkSimilarity(number):

    for i in range(number):
        for j in range(number):
            if i != j:
                str1 = fileNames[i]
                str2 = fileNames[j]
                s = difflib.SequenceMatcher(None, str1, str2).ratio()
                if s > 0.85 and s!= 1.0:
                    print "類似の可能性:", s, "   :",str1, "<-->", str2



def readDatFile():
    global previousName
    for line in open(readData,'r'):
        targetFileLine = line.rsplit(" ",2)
        basename = targetFileLine[0]
        if basename != previousName:
            if len(targetFileLine) > 1 :
                fileNames.append(unicode(targetFileLine[0], 'utf_8'))
        previousName = basename

def decomposit():
    numberofFiles = len(fileNames)
    
    checkSimilarity(numberofFiles)
 


if __name__ == '__main__':
    readDatFile()
    decomposit()
