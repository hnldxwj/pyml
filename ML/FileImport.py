'''
Created on 2015-4-5
@author: hnldxwj
'''
import  copy
class FileImport:

    @staticmethod
    def file2matrix(filename):
        fr=open(filename)
        arrayLines=fr.readlines()
        numsOfLines=len(arrayLines)
        returnMatrix=[]
        for line in arrayLines:
            line=line.strip()
            #print line
            valueFromLine=line.split(' ')
            valueFromLine=[int(x) for x in valueFromLine]
            #print valueFromLine
            returnMatrix.append(valueFromLine)
        fr.close()
        return returnMatrix

    @staticmethod
    def normalization(matrix):
        max=copy.copy(matrix[0])
        min=copy.copy(matrix[0])
        for row in matrix:
            for x in range(1,len(row)):
                if row[x]>max[x]:
                    max[x]=row[x]
                elif row[x]<min[x]:
                    min[x]=row[x]
        #print "max:"+str(max)
        #print "min:"+str(min)
        for row in matrix:
            for x in range(1,len(row)):
                row[x]=(row[x]-min[x])/(max[x]-min[x])

        return matrix


