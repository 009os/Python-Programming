
#Get the mean and standard deviation of the values in math.

import numpy as np
def mean(data):
 n = len(data)
 mean = sum(data) / n
 return mean
def variance(data):
 n = len(data)
 mean = sum(data) / n
 deviations = [(x - mean) ** 2 for x in data]
 variance = sum(deviations) / n
 return variance
def stdev(data):
 import math
 var = variance(data)
 std_dev = math.sqrt(var)
 return std_dev
data = np.array([7,5,4,9,12,45])
print("Standard Deviation of the sample is % s "% (stdev(data)))
print("Mean of the sample is % s " % (mean(data)))
