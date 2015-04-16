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