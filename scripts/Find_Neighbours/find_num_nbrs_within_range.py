from sys import argv
import pickle

geopath = argv[1]
avg_rad_sq = float(argv[2])
twice_rad = avg_rad_sq*4

dct = pickle.load(open(geopath, 'rb'))


def dist(c1, c2):
	return ((c1[0]-c2[0])**2) + ((c1[1]-c2[1])**2)

num_nbr_dict = {}

for k in dct:
	num_nbr_dict[k] = 0

i = 1
for k1 in dct:
	for k2 in dct:
		if dist(dct[k1], dct[k2]) <= twice_rad:
			num_nbr_dict[k1] += 1

	print(i)
	i += 1


pickle.dump(num_nbr_dict, open('num_nbrs.pickle', 'wb'))
			


