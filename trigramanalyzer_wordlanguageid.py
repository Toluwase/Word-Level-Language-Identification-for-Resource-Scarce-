import nltk, re, pprint
from nltk import word_tokenize
from string import punctuation
import string
import sys

#SECTION 1: TRIGRAM EXTRACTION FOR LANGUAGE ONE
fileToOpen=open("C:/Users/Toluwase/Documents/Codon/english_training_corpus.txt","rU", encoding="UTF_8")
fileStream=fileToOpen.read()
tokenList=list()
token_tokenList=list()
fileStreamsmall=fileStream.lower()
frequency={}
mid_trigramList=list()
mid_trigramCountList=list()
bigramList=list()
bigramcountList=list()
wordCountList=list()
trigramProbabilityList=list()
lastWordList=list()
pre_Trigram=list()
pre_TrigramCount=list()
post_Trigram=list()
post_TrigramCount=list()
single_Trigram=list()
single_TrigramCount=list()
all_Trigrams=list()
all_TrigramCount=list()

#to remove numbers and punctuation marks
tokens=word_tokenize(fileStreamsmall)
quotientList=list()
testList=sorted(set(tokens))

#For word list frequency
def getFrequencyDistribution(tokens):
    tokens=word_tokenize(fileStreamsmall)
    for everyToken in tokens:
        count=frequency.get(everyToken, 0)
        frequency[everyToken]=count+1
    return frequency

def printWordsANDFrequency(frequency):
    frequency=getFrequencyDistribution(tokens)
    for abc,bcd in frequency.items():
        print(abc.translate(non_bmp_map),"\t", bcd, "\t", len(abc))

#For Trigram frequency
def getALLTrigrams(frequency):
    frequency=getFrequencyDistribution(tokens)
    for everywordTest in frequency:
        tokenCount=frequency[everywordTest]
        x=0
        for everyletter in everywordTest:
            if len(everywordTest)==2:
                bigram=everywordTest
            elif len(everywordTest)>2:
                if x<len(everywordTest)-2:
                    trigram=everywordTest[x:x+3]
                    x=x+1
                    if trigram in all_Trigrams:
                        trigramIndex5=all_Trigrams.index(trigram)
                        oldTrigramCount5=all_TrigramCount[trigramIndex5]
                        del all_TrigramCount[trigramIndex5]
                        newTrigramCount5=oldTrigramCount5+tokenCount
                        all_TrigramCount.insert(trigramIndex5, newTrigramCount5)
                        #print(trigramCountList[trigramIndex])
                        #do not add trigram to trigram list
                    else:
                        all_Trigrams.append(trigram)
                        all_TrigramCount.append(tokenCount)
    return all_Trigrams, all_TrigramCount

def getPRETrigrams(frequency):
    frequency=getFrequencyDistribution(tokens)
    for everywordTest in frequency:
        tokenCount=frequency[everywordTest]
        x=0
        for everyletter in everywordTest:
            if len(everywordTest)==2:
                bigram=everywordTest
            elif len(everywordTest)>3:
                if x<len(everywordTest)-2:
                    trigram=everywordTest[x:x+3]
                    y=x
                    x=x+1
                    if y==0:
                        if trigram in pre_Trigram:
                            trigramIndex1=pre_Trigram.index(trigram)
                            oldTrigramCount1=pre_TrigramCount[trigramIndex1]
                            del pre_TrigramCount[trigramIndex1]
                            newTrigramCount1=oldTrigramCount1+tokenCount
                            pre_TrigramCount.insert(trigramIndex1, newTrigramCount1)
                            #print(trigramCountList[trigramIndex])
                            #do not add trigram to trigram list
                        else:
                            pre_Trigram.append(trigram)
                            pre_TrigramCount.append(tokenCount)
    return pre_Trigram, pre_TrigramCount

def getMIDTrigrams(frequency):
    frequency=getFrequencyDistribution(tokens)
    for everywordTest in frequency:
        tokenCount=frequency[everywordTest]
        x=0
        for everyletter in everywordTest:
            if len(everywordTest)==2:
                bigram=everywordTest        
            elif len(everywordTest)>3:
                if x<len(everywordTest)-2:
                    trigram=everywordTest[x:x+3]
                    y=x
                    x=x+1
                    if y==0:
                        if trigram in pre_Trigram:
                            trigramIndex1=pre_Trigram.index(trigram)
                            oldTrigramCount1=pre_TrigramCount[trigramIndex1]
                            del pre_TrigramCount[trigramIndex1]
                            newTrigramCount1=oldTrigramCount1+tokenCount
                            pre_TrigramCount.insert(trigramIndex1, newTrigramCount1)
                            #print(trigramCountList[trigramIndex])
                            #do not add trigram to trigram list
                        else:
                            pre_Trigram.append(trigram)
                            pre_TrigramCount.append(tokenCount)
                            #print(trigram)
                            #the end of creating a list of trigrams and trigrams' counts
                            #print (trigram,"\t", everywordTest ,"\t","pre")
                    if y>0 and y<len(everywordTest)-3:
                        if trigram in mid_trigramList:
                            trigramIndex=mid_trigramList.index(trigram)
                            oldTrigramCount=mid_trigramCountList[trigramIndex]
                            del mid_trigramCountList[trigramIndex]
                            newTrigramCount=oldTrigramCount+tokenCount
                            mid_trigramCountList.insert(trigramIndex, newTrigramCount)
                            #print(trigramCountList[trigramIndex])
                            #do not add trigram to trigram list
                        else:
                            mid_trigramList.append(trigram)
                            mid_trigramCountList.append(tokenCount)
    return mid_trigramList, mid_trigramCountList
                    
def getPOSTTrigrams(frequency):
    frequency=getFrequencyDistribution(tokens)
    for everywordTest in frequency:
        tokenCount=frequency[everywordTest]
        x=0
        for everyletter in everywordTest:
            if len(everywordTest)==2:
                bigram=everywordTest
            elif len(everywordTest)>3:
                if x<len(everywordTest)-2:
                    trigram=everywordTest[x:x+3]
                    y=x
                    x=x+1
                    if y==len(everywordTest)-3:
                        if trigram in post_Trigram:
                            trigramIndex2=post_Trigram.index(trigram)
                            oldTrigramCount2=post_TrigramCount[trigramIndex2]
                            del post_TrigramCount[trigramIndex2]
                            newTrigramCount2=oldTrigramCount2+tokenCount
                            post_TrigramCount.insert(trigramIndex2, newTrigramCount2)
                            #print(trigramCountList[trigramIndex])
                            #do not add trigram to trigram list
                        else:
                            post_Trigram.append(trigram)
                            post_TrigramCount.append(tokenCount)
    return post_Trigram, post_TrigramCount

def getSINGLETrigrams(frequency):
    frequency=getFrequencyDistribution(tokens)
    for everywordTest in frequency:
        tokenCount=frequency[everywordTest]
        x=0
        for everyletter in everywordTest:
            if len(everywordTest)==2:
                bigram=everywordTest
            elif len(everywordTest)==3:
                if everywordTest in single_Trigram:
                    trigramIndex3=single_Trigram.index(everywordTest)
                    oldTrigramCount3=single_TrigramCount[trigramIndex3]
                    del single_TrigramCount[trigramIndex3]
                    newTrigramCount3=oldTrigramCount3+tokenCount
                    single_TrigramCount.insert(trigramIndex3, newTrigramCount3)
                    #print(trigramCountList[trigramIndex])
                    #do not add trigram to trigram list
                else:
                    single_Trigram.append(everywordTest)
                    single_TrigramCount.append(tokenCount)
    return single_Trigram, single_TrigramCount

def getTrigramDENOMINATOR(frequency):
    getSINGLETrigrams(frequency)
    getPRETrigrams(frequency)
    getPOSTTrigrams(frequency)
    getMIDTrigrams(frequency)
    frequency=getFrequencyDistribution(tokens)
    denominator=sum(single_TrigramCount)+sum(pre_TrigramCount)+sum(mid_trigramCountList)+sum(post_TrigramCount)
    return denominator

def getPRETrigramsPROBABILITY(pre_Trigram, pre_TrigramCount):
    pre_TrigramPROBABILITYlist=list()
    bcd=0
    frequency=getFrequencyDistribution(tokens)
    getPRETrigrams(frequency)
    denominator=getTrigramDENOMINATOR(frequency)
    for abc in pre_Trigram:
        if bcd<len(pre_Trigram):
            trigramProbability=pre_TrigramCount[bcd]/denominator
            pre_TrigramPROBABILITYlist.append(trigramProbability)
            bcd=bcd+1
    return pre_TrigramPROBABILITYlist

def getMIDTrigramsPROBABILITY(mid_Trigram, mid_TrigramCount):
    mid_TrigramPROBABILITYlist=list()
    cde=0
    frequency=getFrequencyDistribution(tokens)
    getMIDTrigrams(frequency)
    denominator=getTrigramDENOMINATOR(frequency)
    for abc in mid_Trigram:
        if cde<len(mid_Trigram):
            trigramProbability=mid_TrigramCount[cde]/denominator
            mid_TrigramPROBABILITYlist.append(trigramProbability)
            cde=cde+1
    return mid_TrigramPROBABILITYlist

def getPOSTTrigramsPROBABILITY(post_Trigram, post_TrigramCount):
    post_TrigramPROBABILITYlist=list()
    efg=0
    frequency=getFrequencyDistribution(tokens)
    getPOSTTrigrams(frequency)
    denominator=getTrigramDENOMINATOR(frequency)
    for abc in post_Trigram:
        if efg<len(post_Trigram):
            trigramProbability=post_TrigramCount[efg]/denominator
            post_TrigramPROBABILITYlist.append(trigramProbability)
            efg=efg+1
    return post_TrigramPROBABILITYlist


def getSINGLETrigramsPROBABILITY(single_Trigram, single_TrigramCount):
    single_TrigramPROBABILITYlist=list()
    fgh=0
    frequency=getFrequencyDistribution(tokens)
    getSINGLETrigrams(frequency)
    denominator=getTrigramDENOMINATOR(frequency)
    for abc in single_Trigram:
        if fgh<len(single_Trigram):
            trigramProbability=single_TrigramCount[fgh]/denominator
            single_TrigramPROBABILITYlist.append(trigramProbability)
            fgh=fgh+1
    return single_TrigramPROBABILITYlist


def getALLTrigramsPROBABILITY(all_Trigram, all_TrigramCount):
    all_TrigramPROBABILITYlist=list()
    ghi=0
    frequency=getFrequencyDistribution(tokens)
    getALLTrigrams(frequency)
    denominator=getTrigramDENOMINATOR(frequency)
    for abc in all_Trigram:
        if ghi<len(all_Trigram):
            trigramProbability=all_TrigramCount[ghi]/denominator
            all_TrigramPROBABILITYlist.append(trigramProbability)
            ghi=ghi+1
    return all_TrigramPROBABILITYlist
 
#SECTION 1B: THIS PORTION IS OPTIONAL: IT FOR PRINTING ALL THE TYPES OF TRIGRAMS (i.e. PRE, MID, POST, SINGLE & ALL TRIGRAMS)
"""xab, yab=getPRETrigrams(frequency)
t=getPRETrigramsPROBABILITY(xab, yab)
wab=0
for everyz in xab:
    if wab<len(xab)-1:
        print(xab[wab],"\t",yab[wab],"\t", t[wab])
        wab=wab+1

xbc, ybc=getPRETrigrams(frequency)
tbc=getPRETrigramsPROBABILITY(xbc, ybc)
wbc=0
for everyz in xbc:
    if wbc<len(xbc)-1:
        print(xbc[wbc],"\t",ybc[wbc],"\t", tbc[wbc])
        wbc=wbc+1

xcd, ycd=getMIDTrigrams(frequency)
tcd=getMIDTrigramsPROBABILITY(xcd, ycd)
wcd=0
for everyz in xcd:
    if wcd<len(xcd)-1:
        print(xcd[wcd],"\t",ycd[wcd],"\t", tcd[wcd])
        wcd=wcd+1

xde, yde=getPOSTTrigrams(frequency)
tde=getPOSTTrigramsPROBABILITY(xde, yde)
wde=0
for everyz in xde:
    if wde<len(xde)-1:
        print(xde[wde],"\t",yde[wde],"\t", tde[wde])
        wde=wde+1

xef, yef=getSINGLETrigrams(frequency)
tef=getSINGLETrigramsPROBABILITY(xef, yef)
wef=0
for everyz in xef:
    if wef<len(xef)-1:
        print(xef[wef],"\t",yef[wef],"\t", tef[wef])
        wef=wef+1

xfg, yfg=getALLTrigrams(frequency)
tfg=getALLTrigramsPROBABILITY(xfg, yfg)
wfg=0
for everyz in xfg:
    if wfg<len(xfg)-1:
        print(xfg[wfg],"\t",yfg[wfg],"\t", tfg[wfg])
        wfg=wfg+1"""

#SECTION 2: TRIGRAM EXTRACTION FOR LANGUAGE TWO
fileToOpen2=open("C:/Users/Toluwase/Documents/Codon/hausa_corpus.txt","rU", encoding="UTF_8")
fileStream2=fileToOpen2.read()
tokenList2=list()
token_tokenList2=list()
fileStreamsmall2=fileStream2.lower()
frequency2={}
mid_trigramList2=list()
mid_trigramCountList2=list()
bigramList2=list()
bigramcountList2=list()
wordCountList2=list()
trigramProbabilityList2=list()
lastWordList2=list()
pre_Trigram2=list()
pre_TrigramCount2=list()
post_Trigram2=list()
post_TrigramCount2=list()
single_Trigram2=list()
single_TrigramCount2=list()
all_Trigrams2=list()
all_TrigramCount2=list()

#to remove numbers and punctuation marks
tokens2=word_tokenize(fileStreamsmall2)
quotientList2=list()
testList2=sorted(set(tokens2))

#For word list frequency
def getFrequencyDistribution2(tokens2):
    tokens2=word_tokenize(fileStreamsmall2)
    for everyToken2 in tokens2:
        count2=frequency2.get(everyToken2, 0)
        frequency2[everyToken2]=count2+1
    return frequency2

def printWordsANDFrequency2(frequency2):
    frequency2=getFrequencyDistribution2(tokens2)
    for ghi, hij in frequency2.items():
        print(ghi.translate(non_bmp_map),"\t", hij, "\t", len(ghi))

#For Trigram frequency
def getALLTrigrams2(frequency2):
    frequency2=getFrequencyDistribution2(tokens2)
    for everywordTest2 in frequency2:
        tokenCount=frequency2[everywordTest2]
        xya=0
        for everyletter in everywordTest2:
            if len(everywordTest2)==2:
                bigram=everywordTest2
            elif len(everywordTest2)>2:
                if xya<len(everywordTest2)-2:
                    trigram=everywordTest2[xya:xya+3]
                    xya=xya+1
                    if trigram in all_Trigrams2:
                        trigramIndex10=all_Trigrams2.index(trigram)
                        oldTrigramCount10=all_TrigramCount2[trigramIndex10]
                        del all_TrigramCount2[trigramIndex10]
                        newTrigramCount10=oldTrigramCount10+tokenCount
                        all_TrigramCount2.insert(trigramIndex10, newTrigramCount10)
                        #print(trigramCountList[trigramIndex])
                        #do not add trigram to trigram list
                    else:
                        all_Trigrams2.append(trigram)
                        all_TrigramCount2.append(tokenCount)
    return all_Trigrams2, all_TrigramCount2

def getPRETrigrams2(frequency2):
    frequency2=getFrequencyDistribution2(tokens2)
    for everywordTest in frequency2:
        tokenCount=frequency2[everywordTest]
        x=0
        for everyletter in everywordTest:
            if len(everywordTest)==2:
                bigram=everywordTest
            elif len(everywordTest)>3:
                if x<len(everywordTest)-2:
                    trigram=everywordTest[x:x+3]
                    y=x
                    x=x+1
                    if y==0:
                        if trigram in pre_Trigram2:
                            trigramIndex11=pre_Trigram2.index(trigram)
                            oldTrigramCount11=pre_TrigramCount2[trigramIndex11]
                            del pre_TrigramCount2[trigramIndex11]
                            newTrigramCount11=oldTrigramCount11+tokenCount
                            pre_TrigramCount2.insert(trigramIndex11, newTrigramCount11)
                            #print(trigramCountList[trigramIndex])
                            #do not add trigram to trigram list
                        else:
                            pre_Trigram2.append(trigram)
                            pre_TrigramCount2.append(tokenCount)
    return pre_Trigram2, pre_TrigramCount2

def getMIDTrigrams2(frequency2):
    frequency2=getFrequencyDistribution2(tokens2)
    for everywordTest in frequency2:
        tokenCount=frequency2[everywordTest]
        x=0
        for everyletter in everywordTest:
            if len(everywordTest)==2:
                bigram=everywordTest        
            elif len(everywordTest)>3:
                if x<len(everywordTest)-2:
                    trigram=everywordTest[x:x+3]
                    y=x
                    x=x+1
                    if y==0:
                        if trigram in pre_Trigram2:
                            trigramIndex1=pre_Trigram2.index(trigram)
                            oldTrigramCount1=pre_TrigramCount2[trigramIndex1]
                            del pre_TrigramCount2[trigramIndex1]
                            newTrigramCount1=oldTrigramCount1+tokenCount
                            pre_TrigramCount2.insert(trigramIndex1, newTrigramCount1)
                            #print(trigramCountList[trigramIndex])
                            #do not add trigram to trigram list
                        else:
                            pre_Trigram2.append(trigram)
                            pre_TrigramCount2.append(tokenCount)
                            #print(trigram)
                            #the end of creating a list of trigrams and trigrams' counts
                            #print (trigram,"\t", everywordTest ,"\t","pre")
                    if y>0 and y<len(everywordTest)-3:
                        if trigram in mid_trigramList2:
                            trigramIndex=mid_trigramList2.index(trigram)
                            oldTrigramCount=mid_trigramCountList2[trigramIndex]
                            del mid_trigramCountList2[trigramIndex]
                            newTrigramCount=oldTrigramCount+tokenCount
                            mid_trigramCountList2.insert(trigramIndex, newTrigramCount)
                            #print(trigramCountList[trigramIndex])
                            #do not add trigram to trigram list
                        else:
                            mid_trigramList2.append(trigram)
                            mid_trigramCountList2.append(tokenCount)
    return mid_trigramList2, mid_trigramCountList2
                    
def getPOSTTrigrams2(frequency2):
    frequency2=getFrequencyDistribution2(tokens2)
    for everywordTest in frequency2:
        tokenCount=frequency2[everywordTest]
        x=0
        for everyletter in everywordTest:
            if len(everywordTest)==2:
                bigram=everywordTest
            elif len(everywordTest)>3:
                if x<len(everywordTest)-2:
                    trigram=everywordTest[x:x+3]
                    y=x
                    x=x+1
                    if y==len(everywordTest)-3:
                        if trigram in post_Trigram2:
                            trigramIndex2=post_Trigram2.index(trigram)
                            oldTrigramCount2=post_TrigramCount2[trigramIndex2]
                            del post_TrigramCount2[trigramIndex2]
                            newTrigramCount2=oldTrigramCount2+tokenCount
                            post_TrigramCount2.insert(trigramIndex2, newTrigramCount2)
                            #print(trigramCountList[trigramIndex])
                            #do not add trigram to trigram list
                        else:
                            post_Trigram2.append(trigram)
                            post_TrigramCount2.append(tokenCount)
    return post_Trigram2, post_TrigramCount2

def getSINGLETrigrams2(frequency2):
    frequency2=getFrequencyDistribution2(tokens2)
    for everywordTest in frequency2:
        tokenCount=frequency2[everywordTest]
        x=0
        for everyletter in everywordTest:
            if len(everywordTest)==2:
                bigram=everywordTest
            elif len(everywordTest)==3:
                if everywordTest in single_Trigram2:
                    trigramIndex3=single_Trigram2.index(everywordTest)
                    oldTrigramCount3=single_TrigramCount2[trigramIndex3]
                    del single_TrigramCount2[trigramIndex3]
                    newTrigramCount3=oldTrigramCount3+tokenCount
                    single_TrigramCount2.insert(trigramIndex3, newTrigramCount3)
                    #print(trigramCountList[trigramIndex])
                    #do not add trigram to trigram list
                else:
                    single_Trigram2.append(everywordTest)
                    single_TrigramCount2.append(tokenCount)
    return single_Trigram2, single_TrigramCount2

def getTrigramDENOMINATOR2(frequency2):
    getSINGLETrigrams2(frequency2)
    getPRETrigrams2(frequency2)
    getPOSTTrigrams2(frequency2)
    getMIDTrigrams2(frequency2)
    frequency2=getFrequencyDistribution2(tokens2)
    denominator2=sum(single_TrigramCount2)+sum(pre_TrigramCount2)+sum(mid_trigramCountList2)+sum(post_TrigramCount2)
    return denominator2

def getPRETrigramsPROBABILITY2(pre_Trigram2, pre_TrigramCount2):
    pre_TrigramPROBABILITYlist2=list()
    bcd=0
    frequency2=getFrequencyDistribution2(tokens2)
    getPRETrigrams2(frequency2)
    denominator2=getTrigramDENOMINATOR2(frequency2)
    for abc in pre_Trigram2:
        if bcd<len(pre_Trigram2):
            trigramProbability=pre_TrigramCount2[bcd]/denominator2
            pre_TrigramPROBABILITYlist2.append(trigramProbability)
            bcd=bcd+1
    return pre_TrigramPROBABILITYlist2

def getMIDTrigramsPROBABILITY2(mid_Trigram2, mid_TrigramCount2):
    mid_TrigramPROBABILITYlist2=list()
    cde=0
    frequency2=getFrequencyDistribution2(tokens2)
    getMIDTrigrams2(frequency2)
    denominator2=getTrigramDENOMINATOR2(frequency2)
    for abc in mid_Trigram2:
        if cde<len(mid_Trigram2):
            trigramProbability=mid_TrigramCount2[cde]/denominator2
            mid_TrigramPROBABILITYlist2.append(trigramProbability)
            cde=cde+1
    return mid_TrigramPROBABILITYlist2

def getPOSTTrigramsPROBABILITY2(post_Trigram2, post_TrigramCount2):
    post_TrigramPROBABILITYlist2=list()
    efg=0
    frequency2=getFrequencyDistribution2(tokens2)
    getPOSTTrigrams2(frequency2)
    denominator2=getTrigramDENOMINATOR2(frequency2)
    for abc in post_Trigram2:
        if efg<len(post_Trigram2):
            trigramProbability=post_TrigramCount2[efg]/denominator2
            post_TrigramPROBABILITYlist2.append(trigramProbability)
            efg=efg+1
    return post_TrigramPROBABILITYlist2


def getSINGLETrigramsPROBABILITY2(single_Trigram2, single_TrigramCount2):
    single_TrigramPROBABILITYlist2=list()
    fgh=0
    frequency2=getFrequencyDistribution2(tokens2)
    getSINGLETrigrams2(frequency2)
    denominator2=getTrigramDENOMINATOR2(frequency2)
    for abc in single_Trigram2:
        if fgh<len(single_Trigram2):
            trigramProbability=single_TrigramCount2[fgh]/denominator2
            single_TrigramPROBABILITYlist2.append(trigramProbability)
            fgh=fgh+1
    return single_TrigramPROBABILITYlist2


def getALLTrigramsPROBABILITY2(all_Trigram2, all_TrigramCount2):
    all_TrigramPROBABILITYlist2=list()
    ghi=0
    frequency2=getFrequencyDistribution2(tokens2)
    getALLTrigrams2(frequency2)
    denominator2=getTrigramDENOMINATOR2(frequency2)
    for abc in all_Trigram2:
        if ghi<len(all_Trigram2):
            trigramProbability=all_TrigramCount2[ghi]/denominator2
            all_TrigramPROBABILITYlist2.append(trigramProbability)
            ghi=ghi+1
    return all_TrigramPROBABILITYlist2

#SECTION 2B: THIS PORTION IS OPTIONAL: IT FOR PRINTING ALL THE TYPES OF TRIGRAMS (i.e. PRE, MID, POST, SINGLE & ALL TRIGRAMS)
"""xab1, yab1=getPRETrigrams2(frequency2)
t1=getPRETrigramsPROBABILITY2(xab1, yab1)
wab1=0
for everyz in xab1:
    if wab1<len(xab1)-1:
        print(xab1[wab1],"\t",yab1[wab1],"\t", t1[wab1])
        wab1=wab1+1

xbc1, ybc1=getPRETrigrams2(frequency2)
tbc1=getPRETrigramsPROBABILITY2(xbc1, ybc1)
wbc1=0
for everyz in xbc1:
    if wbc1<len(xbc1)-1:
        print(xbc1[wbc1],"\t",ybc1[wbc1],"\t", tbc1[wbc1])
        wbc1=wbc1+1

xcd1, ycd1=getMIDTrigrams2(frequency2)
tcd1=getMIDTrigramsPROBABILITY2(xcd1, ycd1)
wcd1=0
for everyz in xcd1:
    if wcd1<len(xcd1)-1:
        print(xcd1[wcd1],"\t",ycd1[wcd1],"\t", tcd1[wcd1])
        wcd1=wcd1+1

xde1, yde1=getPOSTTrigrams2(frequency2)
tde1=getPOSTTrigramsPROBABILITY2(xde1, yde1)
wde1=0
for everyz in xde1:
    if wde1<len(xde1)-1:
        print(xde1[wde1],"\t",yde1[wde1],"\t", tde1[wde1])
        wde1=wde1+1

xef1, yef1=getSINGLETrigrams2(frequency2)
tef1=getSINGLETrigramsPROBABILITY2(xef1, yef1)
wef1=0
for everyz in xef1:
    if wef1<len(xef1)-1:
        print(xef1[wef1],"\t",yef1[wef1],"\t", tef1[wef1])
        wef1=wef1+1


lmn, mno=getALLTrigrams2(frequency2)
nop=getALLTrigramsPROBABILITY2(lmn, mno)
opq=0
for everyz in lmn:
    if opq<len(lmn)-1:
        print(lmn[opq],"\t",mno[opq],"\t", nop[opq])
        opq=opq+1

#print (x)"""

#SECTION 3: FOR COMPUTING THE NEUTRAL TRIGRAMS (OVERLAPS) BETWEEN TWO LANGUAGES (language1 and language2)
lang1ALLtrigramLIST, lang1ALLcount=getALLTrigrams(frequency)
lang2ALLtrigramLIST, lang2ALLcount=getALLTrigrams2(frequency2)
ALLtrigramsInBoth=set(lang1ALLtrigramLIST).intersection(lang2ALLtrigramLIST)
lang1trigramALLprob=getALLTrigramsPROBABILITY(lang1ALLtrigramLIST, lang1ALLcount)
lang2trigramALLprob=getALLTrigramsPROBABILITY2(lang2ALLtrigramLIST, lang2ALLcount)
"""for abcd in ALLtrigramsInBoth:
    print(abcd)"""

lang1PREtrigramLIST, lang1PREcount=getPRETrigrams(frequency)
lang2PREtrigramLIST, lang2PREcount=getPRETrigrams2(frequency2)
PREtrigramsInBoth=set(lang1PREtrigramLIST).intersection(lang2PREtrigramLIST)
lang1trigramPREprob=getPRETrigramsPROBABILITY(lang1PREtrigramLIST, lang1PREcount)
lang2trigramPREprob=getPRETrigramsPROBABILITY2(lang2PREtrigramLIST, lang2PREcount)
"""for bcde in PREtrigramsInBoth:
    print(bcde)"""

lang1MIDtrigramLIST, lang1MIDcount=getMIDTrigrams(frequency)
lang2MIDtrigramLIST, lang2MIDcount=getMIDTrigrams2(frequency2)
MIDtrigramsInBoth=set(lang1MIDtrigramLIST).intersection(lang2MIDtrigramLIST)
lang1trigramMIDprob=getMIDTrigramsPROBABILITY(lang1MIDtrigramLIST, lang1MIDcount)
lang2trigramMIDprob=getMIDTrigramsPROBABILITY2(lang2MIDtrigramLIST, lang2MIDcount)
"""for cdef in MIDtrigramsInBoth:
    print(cdef)"""

lang1SINGLEtrigramLIST, lang1SINGLEcount=getSINGLETrigrams(frequency)
lang2SINGLEtrigramLIST, lang2SINGLEcount=getSINGLETrigrams2(frequency2)
SINGLEtrigramsInBoth=set(lang1SINGLEtrigramLIST).intersection(lang2SINGLEtrigramLIST)
lang1trigramSINGLEprob=getSINGLETrigramsPROBABILITY(lang1SINGLEtrigramLIST, lang1SINGLEcount)
lang2trigramSINGLEprob=getSINGLETrigramsPROBABILITY2(lang2SINGLEtrigramLIST, lang2SINGLEcount)
"""for defg in SINGLEtrigramsInBoth:
    print(defg)"""

lang1POSTtrigramLIST, lang1POSTcount=getPOSTTrigrams(frequency)
lang2POSTtrigramLIST, lang2POSTcount=getPOSTTrigrams2(frequency2)
POSTtrigramsInBoth=set(lang1POSTtrigramLIST).intersection(lang2POSTtrigramLIST)
lang1trigramPOSTprob=getPOSTTrigramsPROBABILITY(lang1POSTtrigramLIST, lang1POSTcount)
lang2trigramPOSTprob=getPOSTTrigramsPROBABILITY2(lang2POSTtrigramLIST, lang2POSTcount)
"""for efgh in POSTtrigramsInBoth:
    print(efgh)"""

#SECTION4: WORD-LEVEL LANGUAGE IDENTIFICATION
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
punct = set(string.punctuation)
outputList=list()
quotientList=list()

test_tokenList=list()
test_fileToOpen=open("C:/Users/Toluwase/Documents/Codon/EngHau_test_corpus.txt","rU", encoding="UTF-8")
test_fileStream=test_fileToOpen.read()
test_fileStream=test_fileStream.replace(u'\ufeff', '')
test_fileStreamsmall=test_fileStream.lower()
test_tokens=word_tokenize(test_fileStreamsmall)
for everytoken1 in test_tokens:
    newWord1=""
    for everyletter1 in everytoken1:
        if everyletter1 in punct or everyletter1.isdigit():
            everyletter1=""
        else:
            newWord1=newWord1+everyletter1
    newWord2=newWord1
    test_tokenList.append(newWord2)
test_testList=sorted(test_tokenList)
        #print(everytoken)

#to find trigram for test corpus
for test_everywordTest in test_testList:
    a=0
    counter=0
    word_trigramProbability=0
    test_trigramProbability=0.0
    for test_everyletter in test_everywordTest:
        if len(test_everywordTest)==2 or test_everywordTest.isdigit():
            test_bigram=test_everywordTest    
        elif len(test_everywordTest)==3:
            test_trigram=test_everywordTest
            if test_trigram in SINGLEtrigramsInBoth:
                word_trigramProbability=0
                test_trigramProbability=0
                #print(test_trigram)
            elif test_trigram in lang1SINGLEtrigramLIST:
                trigramProbabilityIndex=lang1SINGLEtrigramLIST.index(test_trigram)
                word_trigramProbability=lang1trigramSINGLEprob[trigramProbabilityIndex]
            elif test_trigram in lang2SINGLEtrigramLIST:
                trigramProbabilityIndex=lang2SINGLEtrigramLIST.index(test_trigram)
                word_trigramProbability=-1*(lang2trigramSINGLEprob[trigramProbabilityIndex])
        elif len(test_everywordTest)>3:
            if a<len(test_everywordTest)-2:
                test_trigram=test_everywordTest[a:a+3]
                b=a
                a=a+1
                if b==0:
                    if test_trigram in PREtrigramsInBoth:
                        test_trigramProbability=0
                        word_trigramProbability=word_trigramProbability+test_trigramProbability
                    elif test_trigram in lang1PREtrigramLIST:
                        trigramProbabilityIndex=lang1PREtrigramLIST.index(test_trigram)
                        test_trigramProbability=lang1trigramPREprob[trigramProbabilityIndex]
                        word_trigramProbability=word_trigramProbability+test_trigramProbability
                    #print(test_everywordTest, test_trigram, test_trigramProbability, word_trigramProbability)
                    elif test_trigram in lang2PREtrigramLIST:
                        trigramProbabilityIndex=lang2PREtrigramLIST.index(test_trigram)
                        test_trigramProbability=-1*(lang2trigramPREprob[trigramProbabilityIndex])
                        word_trigramProbability=word_trigramProbability+test_trigramProbability
                if b>0 and b<len(test_everywordTest)-3:
                    if test_trigram in MIDtrigramsInBoth:
                        test_trigramProbability=0
                        word_trigramProbability=word_trigramProbability+test_trigramProbability
                    elif test_trigram in lang1MIDtrigramLIST:
                        trigramProbabilityIndex=lang1MIDtrigramLIST.index(test_trigram)
                        test_trigramProbability=lang1trigramMIDprob[trigramProbabilityIndex]
                        word_trigramProbability=word_trigramProbability+test_trigramProbability
                        #print(test_everywordTest, test_trigram, test_trigramProbability, word_trigramProbability)
                    elif test_trigram in lang2MIDtrigramLIST:
                        trigramProbabilityIndex=lang2MIDtrigramLIST.index(test_trigram)
                        test_trigramProbability=-1*(lang2trigramMIDprob[trigramProbabilityIndex])
                        word_trigramProbability=word_trigramProbability+test_trigramProbability
                if b==len(test_everywordTest)-3:
                    if test_trigram in POSTtrigramsInBoth:
                        test_trigramProbability=0
                        word_trigramProbability=word_trigramProbability+test_trigramProbability
                    elif test_trigram in lang1POSTtrigramLIST:
                        trigramProbabilityIndex=lang1POSTtrigramLIST.index(test_trigram)
                        test_trigramProbability=lang1trigramPOSTprob[trigramProbabilityIndex]
                        word_trigramProbability=word_trigramProbability+test_trigramProbability
                        #print(test_everywordTest, test_trigram, test_trigramProbability, word_trigramProbability)
                    elif test_trigram in lang2POSTtrigramLIST:
                        trigramProbabilityIndex=lang2POSTtrigramLIST.index(test_trigram)
                        test_trigramProbability=-1*(lang2trigramPOSTprob[trigramProbabilityIndex])
                        word_trigramProbability=word_trigramProbability+test_trigramProbability
    if len(test_everywordTest)>2:
        if test_everywordTest in outputList:
            counter=counter+1
        else:
            quotient=word_trigramProbability/len(test_everywordTest)
            outputList.append(test_everywordTest)
            quotientList.append(quotient)
            #wordDictionary[test_everywordTest]=counter+1
            print(test_everywordTest.translate(non_bmp_map),"\t", quotient)
                #print(word_trigramProbability, test_trigram)
                #quotient=word_trigramProbability/len(test_everywordTest)
                #print(test_everywordTest, quotient)

