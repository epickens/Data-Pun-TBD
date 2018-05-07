from collections import Counter
from scipy.stats.stats import pearsonr
import math
from linear_algebra import dot


def mean(x):

    return sum(x) / len(x)


def median(x):

    sorted(x)
    if len(x) % 2 == 1:
        return x[(len(x)+1)/2 - 1]
    else:
        return (x[len(x)/2] + x[len(x)/2 - 1])/2


def quantile(x, per):

    if per == 0:
        return x[0]
    elif per == 1:
        return x[len(x) - 1]
    elif per == 0.5:
        return median(x)
    else:
        return x[len(x)*per]


def mode(x):

    data = Counter(x)
    return data.most_common(1)


def range_x(x):

    sorted(x)
    return x[len(x) - 1] - x[0]


#subtract the mean from each data point
def dif_means(x):
    y = [0] * len(x)
    mean_x = mean(x)
    for i in range(len(x) - 1):
        y[i] = x[i] - mean_x

    return y


#variance
def var(x):
    y = [0] * len(x)
    for i in range(len(x) - 1):
        y[i] = x[i] ^ 2

    #sorted(x)
    return mean(y)


def std_dev(x):

    return math.sqrt(var(x))


#difference between quartiles
def quartile_range(x):

    top = 0.75
    bottom = 0.25

    return quantile(x, top) - quantile(x, bottom)


#covariance
def covar(x, y):

    dotted_difference = dot(dif_means(x), dif_means(y))
    return dotted_difference / (len(x) - 1)


#correlation
def corr(x, y):

    stdev_x = std_dev(x)
    stdev_y = std_dev(y)

    if stdev_x != 0 and stdev_y != 0:
        return covar(x, y) / (stdev_x * stdev_y)
    else:
        return 0
