'''
Created on 2015-4-6
@author: hnldxwj
'''
from math import log
from __future__ import division
from ML import FileImport
class DecisionTree:

    @staticmethod
    def findMajority(dataSet):
        dict={}
        max=0
        for row in dataSet:
            if dict.get[row[0]]==None:
                dict[row[0]]==1
            else:
                dict[row[0]]+=1
        for label,frequency in dict:
            if frequency>max:
                max=frequency
                maxLabel=label
        return maxLabel
            

    @staticmethod
    def calcShannonEnt(dataSet):
        numOfData=len(dataSet)
        labeldict={}
        for row in dataSet:
            if labeldict.get(row[0])==None:
                labeldict[row[0]]=1
            else:
                labeldict[row[0]]+=1
        shannonEnt=0.0
        for key,value in labeldict:
            prob=value/numOfData
            shannonEnt -= prob*log(prob,2)
        return shannonEnt
    
    @staticmethod
    def splitDataSet(dataSet,column,value):
        resultSet=[]
        for row in dataSet:
            if row[column]==value:
                NeedRow=row[:column]
                NeedRow.extend(row[column+1:])
                resultSet.append(NeedRow)
        return resultSet
    
    @staticmethod
    def chooseBestSplitMethod(dataSet):
        baseEntropy=DecisionTree.calcShannonEnt(dataSet)
        bestEntopy=baseEntropy
        bestColumn=0
        for x in range(1,len(dataSet[0])):
            valList=[row[0] for row in dataSet]
            valSet=set(valList)
            newEntropy=0.0
            #calculate (columu x)'s Shannon Entropy
            for val in valSet:
                subDataSet=DecisionTree.splitDataSet(dataSet,x,val)
                newEntropy+=(len(subDataSet)/len(dataSet))*DecisionTree.calcShannonEnt(subDataSet)
            if newEntropy<bestEntopy:
                bestEntopy=newEntropy
                bestColumn=x
        if bestColumn==0:
            print "Column Error!!!"
        
        return bestColumn   
        
    @staticmethod
    def createTree(dataSet):
        labelList=[row[0] for row in dataSet]
        labelSet=set(labelList)
        # same label
        if len(labelSet)==1:
            return labelSet[0]
        #only one column
        if len(dataSet[0])==1:
            return DecisionTree.findMajority(dataSet)
        bestColumn=DecisionTree.chooseBestSplitMethod(dataSet)
        
        tree={bestColumn:{}}
        bestColumnValList=[row[bestColumn] for row in dataSet]
        bestColumnValSet=set(bestColumnValList)
        for val in bestColumnValSet:
            tree[bestColumn][val]=DecisionTree.createTree(DecisionTree.splitDataSet(dataSet,bestColumn,val))
        return tree


    @staticmethod
    def findDecisonTreeResult(tree,test):

        return


    @staticmethod
    def calc(trainfile,testfile,outputfile):

        trainset=FileImport.file2matrix(trainfile)
        testset=FileImport.file2matrix(testfile)
        fw=open(outputfile,'w')
        tree=DecisionTree.createTree(trainset)
        for row in testset:
            result=DecisionTree.findDecisonTreeResult(tree,row)
            #print "result:"+str(result)
            fw.write(str(result)+"\n")
        fw.close()
        return True
            
        