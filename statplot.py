# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:41:31 2018

@author: Dylan
"""
import random, pylab, numpy as np

def makeHist(data, title, xlabel, ylabel, bins = 20):
    """Makes histogram"""
    pylab.hist(data, bins = bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    
    
def sampleMean(data, n):
    """calculates a sample mean given a list 
    of data and n samples from the list chosen 
    without replacement"""
    return np.mean(random.sample(data,n))

def sampleMeans(data, numMeans, numSamplesPerMean):
    meanList = []
    for x in range(0, numMeans):
        meanList.append(sampleMean(data, numSamplesPerMean))
    
    return meanList

def getMeansAndSDs(population, sample, verbose = False):
    popMean = sum(population)/len(population)
    sampleMean = sum(sample)/len(sample)
    if verbose:
        makeHist(population,
                 'Population' +\
                 '(mean = '  + str(round(popMean, 2)) + ')',
                 '', '')
        pylab.figure()
        makeHist(sample, 'Sample\n' +\
                 '(mean = ' + str(round(sampleMean, 2)) + ')',
                 '', '')   
        print('Population mean =', popMean)
        print('Standard deviation of population =',
              np.std(population))
        print('Sample mean =', sampleMean)
        print('Standard deviation of sample =',
              np.std(sample))
    return (popMean, sampleMean, np.std(population), np.std(sample))

def sem(popSD, sampleSize):
    return popSD/sampleSize**0.5

