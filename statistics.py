from collections import Counter
from scipy.stats.stats import pearsonr


def mean(x):

    sum(x) / len(x)


def median(x):

    sorted(x)
    if len(x)%2 == 1:
        return x[(len(x)+1)/2 - 1]
    else:
        return (x[len(x)/2] + x[len(x)/2 - 1])/2


def quantile(x, per):

    if per == 0:
        return x[0]
    elif per == 100:
        return x[len(x) - 1]
    elif per == 50:
        return median(x)
    else:
        return x[len(x)*per]


def mode(x):

    data = Counter(x)
    return data.most_common(1)


def range(x):

    sorted(x)
    return x[len(x) - 1] - x[0]


#subtract the mean from each data point
def dif_means(x):

    for i in range (0, len(x) - 1):
        x[i] = x[i] - mean(x)

    return x


#variance
def var(x):

    for i in range (0, len(x) - 1):
        x[i] = x[i]^2

    sorted(x)
    return mean(x)


def std_dev(x):

    return var(x)^(1/2)


#difference between quartiles
def quartile_range(x):

    top = 100 - x/2
    bottom = x/2

    return quantile(x, top) - quantile(x, bottom)


#covariance
def covar(x, y):

    return numpy.cov(x, y)[0][1]


#correlation
def corr(x, y):

    return pearsonr(x, y)