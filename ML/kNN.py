'''
Created on 2015-4-4
@author: hnldxwj
'''

from FileImport import FileImport
from DataStructure import Node
from DataStructure import BinarySearchArray

class kNN:

        @staticmethod
        def calc(trainfile,testfile,outputfile,k):
            if k==0:
                return False
            trainset=FileImport.file2matrix(trainfile)
            trainset=FileImport.normalization(trainset)
            testset=FileImport.file2matrix(testfile)
            testset=FileImport.normalization(testset)
            fw=open(outputfile,'w')
            for row in testset:
                result=kNN.calcOneCase(trainset,row,k)
                #print "result:"+str(result)
                fw.write(str(result)+"\n")
            fw.close()
            return True
  

        @staticmethod
        def calcOneCase(trainset,testrow,k):

            bsa=BinarySearchArray(k)
            bsa.setType(1)
            for trainrow in trainset:
                distance=kNN.calcDistance(trainrow,testrow)
                node=Node(distance,trainrow[0])
                bsa.insert(node)

            return bsa.findMost()

        @staticmethod
        def calcDistance(trainrow,testrow):
            val=0
            for x in range(1,min(len(trainrow),len(testrow))):
                val+=((trainrow[x]-testrow[x])**2)
            val=val**0.5
            return val



