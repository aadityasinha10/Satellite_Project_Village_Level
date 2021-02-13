import pandas as pd
import pickle

bf_out = pickle.load(open('./input/bf_out.pickle', 'rb'))
fc_out = pickle.load(open('./input/fc_out.pickle', 'rb'))
msw_out = pickle.load(open('./input/msw_out.pickle', 'rb'))
asset_out = pickle.load(open('./input/asset_out.pickle', 'rb'))
comb_dict = pickle.load(open('./combined_dict.pickle', 'rb'))
nl_dict = pickle.load(open('./nl_input.pickle', 'rb'))

out_list = [bf_out, fc_out, msw_out, asset_out]
ind_list = ['BF', 'FC', 'MSW', 'ASSET']

columns = ['Village_ID']
for i in range(6):
	for ind in ind_list:
		for j in range(1,4):
			columns += ['{}_{}_OUT_{}'.format(ind, i, j)]
columns += ['Total_Light', 'Total_Light_Cal', 'Max_Light']


df = pd.DataFrame(0.0, index = [i for i in range(len(comb_dict))], columns = columns)
print(df.columns)

print()
print("Length:", len(df))
print(df.iloc[0])
print()

id = 0

from tqdm import tqdm
for vill in tqdm(comb_dict):
	
	df.iloc[id, 0] = vill
	col_num = 1

	for nbr in comb_dict[vill]:
		for out_i in range(len(out_list)):
			out_dct = out_list[out_i]
			if nbr in out_dct:
				for fin_out in out_dct[nbr]:
					df.iloc[id, col_num] = fin_out
					col_num += 1
			else:
				col_num += 3

	if vill in nl_dict:
		for dat in nl_dict[vill]:
			df.iloc[id, col_num] = dat
			col_num += 1

	id += 1


print(df.iloc[0])
pickle.dump(df, open('final_input.pickle', 'wb'))


	
	
	
	


