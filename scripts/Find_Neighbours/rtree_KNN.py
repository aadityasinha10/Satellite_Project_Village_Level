import pickle
import sys
from rtree import index
from time import time

ind = sys.argv[1]
dct = pickle.load(open('dicts/{}_ids'.format(ind), 'rb'))

def generator():
    for k in dct:
        yield(k, (dct[k][0], dct[k][1], dct[k][0], dct[k][1]), dct[k][0])

start = time()
tree = index.Index(generator())
print("Time taken to bulkload is:", time()-start)

count = 0
start = time()
out_dct = {}

for k in dct:
    out_dct[k] = list(tree.nearest((dct[k][0], dct[k][1], dct[k][0], dct[k][1]), 6))
    count += 1

end = time()
print("Time taken to find KNN for each point:", end-start)
print("#Points:", count)

pickle.dump(out_dct, open('NBRS/nbrs_{}.pickle'.format(ind), 'wb'))
