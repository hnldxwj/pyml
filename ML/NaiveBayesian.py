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

    #@staticmethod
    #def