import pandas as pd
import sys
import numpy as np
import math
from collections import defaultdict, Counter
from functools import partial
#Please check the readme before running


#Entropy functions
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
    groups = data.groupby(feature)
    return [groups.get_group(x) for x in groups.groups]


#get partition statistic (either entropy or chi-square)
def get_part_stat(data, feature, stat="entropy"):
    partitions = get_partition(data, feature)
    if stat == "entropy":
        return part_entropy(partitions)
    else:
        return part_chi(partitions)


#Chi-Squared
def get_chi(x):
    y = x.iloc[:,-1]
    len_y = len(y.index)
    counts = [count for count in Counter(y).values()]
    return sum(((count - len_y/2)**2 / (len_y/2))**0.5 for count in counts)


def part_chi(data):
    #Data is a set of subsets
    return sum(get_chi(subset) for subset in data)


#Classifier Functions
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


def make_tree(data, splits=None, stat="entropy"):
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

    best_split = min(splits, key=partial(get_part_stat, data, stat=stat))

    partitions = get_partition(data, best_split)

    future_splits = [s for s in splits if s != best_split]

    child_trees = {subset[[best_split]].values[0][0]: make_tree(subset, future_splits) for subset in partitions}

    child_trees[None] = tot_true > tot_false

    return best_split, child_trees


def classify(tree, input):
    if tree in [True, False]:
        return tree
    traversal_key = None
    for key in tree[1].keys():
        #print("{} == {}".format(tree[0], key))
        for val in input:
            if key == val: traversal_key = key
    return classify(tree[1][traversal_key], input)


def print_tree(tree, level=0):
    tab = "\t" * level
    if tree in [True, False]:
        print("{}{}".format(tab, tree))
        return tree
    for key in tree[1].keys():
        if key is None:
            break
        print("{}{} == {}".format(tab, tree[0], key))
        print_tree(tree[1][key], level+1)


#Leave one out cross validation
def loocv_tree(data, stat="entropy"):
    trees = []

    for i in range(data.shape[0]):
        loo_data = data.drop([i], axis=0)
        trees.append(make_tree(loo_data, stat=stat))

    accuracies = []
    for tree in trees:
        accuracies.append(get_accuracy(tree, data))

    #Return the tree the preforms best on the entire dataset
    return trees[accuracies.index(max(accuracies))]


#Get Accuracies
def get_accuracy(tree, data):
    validation_set = []
    for label in data.iloc[:,-1]:
        if label == "yes":
            validation_set.append(True)
        else:
            validation_set.append(False)

    pred = []
    for index, row in data.iterrows():
        pred.append(classify(tree, row))

    tot_correct = 0
    for i in range(len(pred)):
        if pred[i] == validation_set[i]:
            tot_correct += 1

    return tot_correct / len(pred)


data = pd.read_csv(sys.argv[1], sep="\t")
tree = make_tree(data, stat="chi")
"""test = data.sample().values[0]
print(test)
print(classify(tree, test))
test1 = data.sample().values[0]
print(test1)
print(classify(tree, test1))"""
print("\nRegular Chi-Squared Tree\n")
print_tree(tree)
print("\nLOOCV Tree (Entropy)\n")
print_tree(loocv_tree(data))