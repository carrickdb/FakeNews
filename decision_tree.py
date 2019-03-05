# from sklearn import tree
import csv, random
import numpy as np
import matplotlib.pyplot as plt

Xcon = []

with open("vectors_erraticism_con.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        Xcon.append(row[1])

# Xcon = Xcon[:20]
ycon = [0 for i in range(len(Xcon))]

Xlib = []
# ylib = []
with open("vectors_erraticism_lib.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        Xlib.append(row[1])

# Xlib = Xlib[:20]
ylib = [1 for i in range(len(Xlib))]
print(len(Xlib))

plt.scatter(Xcon, ycon, color='red')
plt.scatter(Xlib, ylib, color='blue')
plt.xticks(np.arange(0, 1, 1))
plt.show()



# clf = tree.DecisionTreeClassifier(random_state=0, max_depth=3)
# estimator = clf.fit(X, y)
#
# # From https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#sphx-glr-auto-examples-tree-plot-unveil-tree-structure-py
# n_nodes = estimator.tree_.node_count
# children_left = estimator.tree_.children_left
# children_right = estimator.tree_.children_right
# feature = estimator.tree_.feature
# threshold = estimator.tree_.threshold
#
# # The tree structure can be traversed to compute various properties such
# # as the depth of each node and whether or not it is a leaf.
# node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
# is_leaves = np.zeros(shape=n_nodes, dtype=bool)
# stack = [(0, -1)]  # seed is the root node id and its parent depth
# while len(stack) > 0:
#     node_id, parent_depth = stack.pop()
#     node_depth[node_id] = parent_depth + 1
#
#     # If we have a test node
#     if (children_left[node_id] != children_right[node_id]):
#         stack.append((children_left[node_id], parent_depth + 1))
#         stack.append((children_right[node_id], parent_depth + 1))
#     else:
#         is_leaves[node_id] = True
#
# print("The binary tree structure has %s nodes and has "
#       "the following tree structure:"
#       % n_nodes)
# for i in range(n_nodes):
#     if is_leaves[i]:
#         print("%snode=%s leaf node." % (node_depth[i] * "\t", i))
#     else:
#         print("%snode=%s test node: go to node %s if X[:, %s] <= %s else to "
#               "node %s."
#               % (node_depth[i] * "\t",
#                  i,
#                  children_left[i],
#                  feature[i],
#                  threshold[i],
#                  children_right[i],
#                  ))
