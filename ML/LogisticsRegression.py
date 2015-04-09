from math import exp

class LogisticsRegression:

    @staticmethod
    def sigmoid(z):
        return 1.0/(1+exp(-z))

    @staticmethod
    def gradAscent():
        return