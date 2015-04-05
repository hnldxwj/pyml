'''
Created on 2015-4-4
@author: hnldxwj
'''

from FileImport import FileImport

class kNN:

       @staticmethod
       def calc(trainfile,testfile,outputfilename):
           trainset=FileImport.file2matrix(trainfile)
           trainset=FileImport.normalization(trainset)
           testset=FileImport.file2matrix(testfile)
           testset=FileImport.normalization(testfile)
           fw=open(outputfilename,'w')
           for row in testset:
               result=kNN.calcOneCase(trainset,row)
               fw.write(str(result)+"\n")
           fw.close()
           return


       @staticmethod
       def calcOneCase(trainset,testrow):


           return




