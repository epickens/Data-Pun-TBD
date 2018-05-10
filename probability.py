from collections import Counter
import math, random
from scipy.stats import norm
from scipy.special import gammainc


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
    #check for rescaling
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z_score = -15
    high_z_score = 15
    avg_z_score = (low_z_score + high_z_score) / 2

    while high_z_score - low_z_score > tolerance:
        avg_pval = normal_cdf(avg_z_score)
        avg_z_score = (low_z_score + high_z_score) / 2

        if avg_pval > p:
            high_z_score = avg_z_score
        elif avg_pval < p:
            low_z_score = avg_z_score
        else:
            break

    return avg_zscore


def bernoulli_trial(p):
    if random.random() > p:
        return 0
    else:
        return 1


def binomial(p, n):
    sum_trials = sum(bernoulli_trial(p) for _ in range(n))
    return sum_trials


def geometric_pdf(p, k, failures=False):
    if failures:
        exp_term = (1 - p) ^ k
        return exp_term * p
    else:
        exp_term = (1 - p) ^ (k -1)
        return exp_term * p


def geometric_cdf(p, k, failures=False):
    if failures:
        return 1 - (1 - p) ^ (k + 1)
    else:
        return 1 - (1 - p) ^ k


def poisson_pdf(lam, k):
    return lam ^ k * math.exp(-lam)/math.factorial(k)


def poisson_cdf(lam, x):
    cdf = 0
    for x in range(x, 0):
        cdf += poisson_pdf(lam, x)

    return cdf


def gamma_function(n):
    return math.factorial(n-1)


def gamma_pdf(k, theta, x):
    coef = 1 / (gamma_function(k) * (theta) ^ k)
    e_term = math.exp(- (x / theta))
    x_term = x ^ (k - 1)

    return coef * x_term * e_term


def gamma_cdf(k, theta, x):
    #gamma = 1 / gamma_function(k)
    #incomp_gamma = incomp_gamma_function(a, k)
    #need to implement a version of the imcomplete gamma function
    #but I'm not sure how to rn
    #so I'm taking the easy way out
    return gammainc(k, x / theta)


def exponential_pdf(lam, x):
    return lam * math.exp(-1 * lam * x)


def exponential_cdf(lam, x):
    return 1 - exponential_pdf(lam, x)


def discrete_expectation(x, p):
    return dot(x, p)
