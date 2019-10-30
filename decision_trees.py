import pandas as pd
import sys
import numpy as np
import math
from collections import defaultdict, Counter
from functools import partial


data = pd.read_csv(sys.argv[1], sep="\t")

print(data.head())


def entropy_eqn(probs):
    return sum(-p * math.log(p, 2) for p in probs if p)


def get_probs(y):
    len_y = len(y.index)
    return [count / len_y for count in Counter(y).values()]


def get_entropy(x):
    probs = get_probs(x.iloc[:,-1])
    return entropy_eqn(probs)


def part_entropy(data):
    #Data is a set of subsets

    tot_len =  sum(len(subset.index) for subset in data)

    return sum(get_entropy(subset) * len(subset.index) / tot_len for subset in data)


def get_partition(data, feature):

    """
    groups = defaultdict(list)
    for row in data.iterrows():
        key = row[['feature']]
        groups[key].append(row)
    return groups
    """

    groups = data.groupby(feature)
    return [groups.get_group(x) for x in groups.groups]

def get_part_entropy(data, feature):
    partitions = get_partition(data, feature)
    return part_entropy(partitions)


def dt_classifier(tree, data):
    #leaf node base case
    if tree in [True, False]:
        return tree

    #o/w we have more features to split on and feature values
    feature, child_dict = tree

    child_key = data.get(feature)

    if child_key not in child_dict:
        child_key = None

    child = child_dict[child_key]
    return dt_classifier(child, data)


def make_tree(data, splits=None):

    if splits is None:
        splits = data.iloc[:,:-1].columns

    df_height = len(data.index)
    tot_true = df_height - len(data[data.iloc[:,-1] == 'no'])
    tot_false = df_height - tot_true

    if tot_true == 0:
        return False
    if tot_false == 0:
        return True

    if len(splits) == 0:
        return tot_true >= tot_false

    best_split = min(splits, key=partial(get_part_entropy, data))

    partitions = get_partition(data, best_split)

    future_splits = [s for s in splits if s != best_split]

    child_trees = {subset[[best_split]].values[0][0] : make_tree(subset, future_splits) for subset in partitions}

    child_trees[None] = tot_true > tot_false

    return best_split, child_trees


print(data.dtypes)
tree = make_tree(data)
print(tree)
