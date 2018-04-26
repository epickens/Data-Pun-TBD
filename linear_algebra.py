def add_vectors(v, w):


def subtract_vectors(v, w):


def vector_sum(vecs):


def scalar_multiplication(c, v):


def vector_mean(vecs):


def dot(v, w):


def sum_of_sqrs(v):


def magnitude(v):


def squared_distance(v, w):


def distance(v, w):


def shape(A):


def get_row(A, i):

    row_list = []
    for x in range(0, len(A[i])):
        row_list.append(A[i][x])

    return row_list

def get_column(A, j):

    colum_list = []
    for x in range(0, len(A[j]):
        colum_list.append(A[x][j])

    return colum_list

def make_matrix(num_rows, num_cols, entry_fn):


def is_identity(A):

    for x in range(0, len(A)):
        for y in range(0, len(A[x])):
            if x == y:
                if A[x][y] != 1:
                    return False
            if x != y:
                if A[x][y] != 0:
                    return False

    return True

def matrix_add(A, B):

    w, h = len(A[0]), len(A);
    new_matrix = [[0 for x in range(w)] for y in range(h)]
    for x in range (0, len(A)):
        for y in range (0, len(A[x])):
            new_matrix[x][y] = A[x][y] + B[x][y]

    return new_matrix