from functools import reduce
import math


def add_vectors(v, w):
    if len(v) != len(w):
        raise ArithmeticError("These vectors are not of the same size")

    new_list = [v_i + w_i for v_i, w_i in zip(v, w)]
    return new_list


def subtract_vectors(v, w):
    if len(v) != len(w):
        raise ArithmeticError("These vectors are not of the same size")

    new_list = [v_i - w_i for v_i, w_i in zip(v, w)]
    return new_list


def vector_sum(vecs):
    return reduce(add_vectors, vecs)


def scalar_multiplication(c, v):
    new_list = [c * v_i for v_i in v]

    return new_list


def vector_mean(vecs):
    num_elements = len(vecs)

    new_list = scalar_multiplication(1/num_elements, vector_sum(vecs))

    return new_list


def dot(v, w):

    sum = (v_i * w_i for v_i, w_i in zip(v, w))

    return sum


def sum_of_sqrs(v):

    ssqrs = dot(v, v)

    return ssqrs

def magnitude(v):

    mag = math.sqrt(sum_of_sqrs(v))

    return mag


def squared_distance(v, w):

    sqr_dist = sum_of_sqrs(subtract_vectors(v, w))

    return sqr_dist


def distance(v, w):

    dist = math.sqrt(squared_distance(v, w))

    return  dist


def shape(A):


def get_row(A, i):


def get_column(A, j):


def make_matrix(num_rows, num_cols, entry_fn):


def is_identity(A):


def matrix_add(A, B):


