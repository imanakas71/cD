#!/usr/bin/env python
#coding:utf-8
import unicodedata
import difflib
import os
import sys
from decimal import (Decimal, ROUND_DOWN)
dirNames=[]
fileNames = []
dict={}
numberofFiles = 0
previousName = ''
readData = 'books.txt'
fromBase=[]
toBase=[]

def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch) 
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False

def putCandidateCommand():
    from os.path import join, getsize
    for root, dirs, files in os.walk('.'):
        pass
def checkSimilarity(number):

    for i in range(number):
        str1 = fileNames[i]
        if is_japanese(str1) == False:
            continue
        for j in range(number):
            str2 = fileNames[j]
            if is_japanese(str2) == False:
                continue
            if i != j:
                s = difflib.SequenceMatcher(None, str1, str2).ratio()
                if s > 0.85 and s!= 1.0:
                    v = Decimal(s).quantize(Decimal('0.001'), rounding=ROUND_DOWN)
                    x1 = dict[str1]
                    x2 = dict[str2]
                    if x1 > x2 :
                        print u"類似の可能性: "+ str(v).decode('utf-8')+ u"   :"+str1+"("+str(x1).decode('utf-8')+")"+ "<-->"+str2+"("+str(x2).decode('utf-8')+")"
                        fromBase.append[str1]
                        toBase.append[str2]


def readDatFile(fileName):
    global previousName
    for line in open(fileName,'r'):
        targetFileLine = line.rsplit(" ",2)
        basename = targetFileLine[0].decode('utf-8')
        if basename != previousName:
            if len(targetFileLine) > 1 :
                fileNames.append(basename)
                dict[basename]=1
        else:
            dict[basename]=dict[basename]+1
        previousName = basename

def decomposit():
    numberofFiles = len(fileNames)
    checkSimilarity(numberofFiles)
 


if __name__ == '__main__':
    os.environ["PYTHONIOENCODING"]='utf-8'
    argv = sys.argv
    length = len(argv)
    if length == 2:
        readData = argv[1]
        print u"Reading "+argv[1]
    readDatFile(readData)
    decomposit()
