import pickle
import os

comb_dict = {}

for fl in os.listdir('./NBRS'):
	dct = pickle.load(open('./NBRS/'+fl, 'rb'))
	
	for k in dct:
		if k not in comb_dict:
			comb_dict[k] = dct[k]


print("Length of comb dict:", len(comb_dict))
pickle.dump(comb_dict, open('combined_dict.pickle', 'wb'))
			
