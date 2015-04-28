from FileImport import FileImport
class NaiveBayesian:

    @staticmethod
    def loadDataSet():

        return

    @staticmethod
    def createWordList(dataSet):
        WordSet=set([])
        for data in dataSet:
            WordSet=WordSet | set(data) #combination
        return list(WordSet)



    @staticmethod
    def findWordInInput(dataSet,InputSet):
        returnArray=[0]*dataSet
        for word in InputSet:
            if word in dataSet:
                returnArray[dataSet.index(word)]=1
        return returnArray


    @staticmethod
    def findAllFeature(dataSet,index):
        theList=[ x[index] for x in dataSet]
        theSet=set(theList)
        return theSet

    # calc every P(label|feature)
    @staticmethod
    def findLabel2Feature(dataSet,index,feature):
        possible={}
        for l in dataSet:
            if l[index]==feature:
                if possible.get(l[0])!=None:
                    possible[l[0]]+=1
                else:
                    possible[l[0]]=1

        count=0
        for label,val in possible:
            count+=val
        res={}
        for label,val in possible:
            res[label]=val*1.00/count
        return res


    @staticmethod
    def findBiggestPosibility(model,test):

        return


    @staticmethod
    def calc(trainfile,testfile,outputfile):

        trainset=FileImport.file2matrix(trainfile)
        testset=FileImport.file2matrix(testfile)
        fw=open(outputfile,'w')

        # model(list)-->index(dict)--> feature(dict)--> label(posiibility)
        model=[]
        for i in range(trainset[0]):
            featureset=NaiveBayesian.findAllFeature(trainset,i)
            index={}
            for f in featureset:
                index[f]=(NaiveBayesian.findLabel2Feature(trainset,i,f))
            model.append(index)

        for row in testset:
            result=NaiveBayesian.findBiggestPosibility(model,row)
            #print "result:"+str(result)
            fw.write(str(result)+"\n")
        fw.close()
        return True
