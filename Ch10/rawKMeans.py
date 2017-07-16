#-*- coding:utf-8 -*-

from numpy import *

def loadDataSet(fileName):
    dataSet = []
    with open(fileName) as fr:
        for line in fr.readlines():
            curLine = line.strip().split('\t')
            fltLine = list(map(float, curLine))
            dataSet.append(fltLine)
    return dataSet

def distance_Eud(Vec_A,Vec_B):
    return sqrt(sum(power((Vec_A - Vec_B),2)))

#give random mean dot
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    # k*n 2-D 
    centroids = mat(zeros((k,n)))
    #if the location is (x,y); 
    #so first the value will be given to x, then y;
    #here we get new center
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)
    return centroids

#give the KMeans algorithm Simple version.
def Kmeans(dataSet, k, distMeans= distance_Eud, createCent = randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    #create center number: k
    centroids = createCent(dataSet,k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        #loops in row, location -> x
        for i in range(m):
            minDist = inf
            minIndex = -1
            #loops in row, number= k, there are k centers
            for j in range(k):
                #calculate the distance between (x,y) and center
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                #get the minium distance, and index
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        print(centroids)
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent,:] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment

#this is the biKMeans algorithm
def biKMeans(dataSet, k, disMean= distance_Eud):
    m = shape(dataSet)[0]
    #create a zore matrix to help measureing the sqrt distance
    clusterAssment = mat(zeros((m,2)))
    #calculate mean of columns(contains two indexs) location:(x,y)
    #the mean of (x,y),here it is. centroid0 is an Array!!!
    centroid0 = mean(dataSet, axis= 0).tolist()[0]
    centList = [centroid0]
    #distance between every dot and centroid0. record
    for j in range(m):
        clusterAssment[j,1] = disMean(mat(centroid0), dataSet[j,:])**2

    while(len(centList) < k):
        lowestSSE = inf

        for i in range(len(centList)):
            #get the rows of which value equals to i
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A == i)[0],:]
            #get center and assemnt when divide into 2 parts
            centroidMat, splitClustAss = Kmeans(ptsInCurrCluster, 2, disMean)
            #SSE of two
            sseSplit = sum(splitClustAss[:,1])
            #SSE of one cluster
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A != i)[0], 1])
            
    print("sseSplit:{0}, sseNotSplit:{1}".format(sseSplit, sseNotSplit))
    if (sseSplit + sseNotSplit) < lowestSSE:
        bestCentToSplit = i
        bestNewCents = centroidMat
        bestClustAss = splitClustAss.copy()
        lowestSSE = sseSplit + sseNotSplit

    bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList)
    bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentTopSplit
    print('the bestCentToSplit is:', bestCentToSplit)
    print('the len of bestClustAss is:', len(bestClustAss))
    centList[bestCentTosplit] = bestNewCents[0,:]
    centerAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:]= bestClustAss
    return mat(centList), clusterAssment
