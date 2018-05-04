from collections import Counter
import math, random
from scipy.stats import norm

def uniform_pdf(x):
    if x < 1 and x >= 0:
        return 1
    else:
        return 0


def uniform_cdf(x):
    if x <= 0:
        return 0
    elif x <1:
        return x
    else:
        return 1


def normal_pdf(x, mu=0, sigma=1):
    coef = 1 / math.sqrt(2 * math.pi * (sigma ^ 2))
    exp_term = math.exp(- ((x - mu) ^ 2) / (2 * (sigma ^ 2)))
    return coef * exp_term


def normal_cdf(x, mu=0, sigma=1):
    err = math.erf((x - mu) / (sigma * math.sqrt(2)))
    return 0.5 * (1 + err)


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    norm.ppf(p)


def bernoulli_trial(p):
    if random.random() > p:
        return 0
    else:
        return 1


def binomial(p, n):
    sum = sum(bernoulli_trial(p) for _ in range(n))
    return sum