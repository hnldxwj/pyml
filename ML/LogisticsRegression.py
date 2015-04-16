from math import exp
from numpy import *

class LogisticsRegression:


    @staticmethod
    def sigmoid(z):
        return 1.0/(1+exp(-z))

    @staticmethod
    def gradAscent(dataIn,labelIn):
        dataMatrix=mat(dataIn)
        labelMatrix=mat(labelIn).transpose()
        maxCycle=500
        alpha=0.01
        m,n=shape(dataMatrix)
        weight=ones({n,1})
        for x in xrange(maxCycle):
            h=LogisticsRegression.sigmoid(dataMatrix*weight)
            error=(labelMatrix-h)
            weight=weight+alpha*dataMatrix.transpose()*error


        return weight