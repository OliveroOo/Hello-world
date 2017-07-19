#-*-coding utf-8 -*-
'''
2017/7/18
author zihao
'''

from numpy import *

#load DataSet
def loadDataSet(fileName, delimeter= '\t'):
    with open(fileName) as fr:
        stringArr = [line.strip().split(delimeter) for line in fr.readlines()]
        dataArr = [list(map(float,line)) for line in stringArr]
    return mat(dataArr)

#pac algorithem
def pca(dataArr, topNfeat= 999999):
    meanVals = mean(dataMat, axis=0)
    #remove the mean values
    meanRemoved = dataMat - meanVals
    #cov calculate
    covMat = cov(meanRemoved, rowvar=0)
    eigVals, eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    redEigVects = eigVects[:,eigValInd]
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat


if __name__ == "__main__":
    dataMat = loadDataSet('testSet.txt')
    lowDData, reconMat = pca(dataMat, 1)
    shape(lowDData)
    import matplotlib
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0],marker='^', s=90)
    ax.scatter(reconMat[:,0].flatten().A[0], reconMat[:,1].flatten().A[0],marker='o', s=50, c='red')
    plt.show()

