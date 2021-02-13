import pandas as pd
from sys import argv
import os

columns = ['VILLAGE CODE','NUMBER OF PRIMARY SCHOOLS', 'NUMBER OF MIDDLE SCHOOLS', 'NUMBER OF COLLEGES', 'NUMBER OF ALLOPATHIC HOSPITALS', 'NUMBER OF MATERNITY AND CHILD WELFARE CENTRES', 'NUMBER OF PRIMARY HEALTH CENTER', 'NUMBER OF POST OFFICES', 'NUMBER OF TELEPHONE CONNECTIONS', 'NUMBER OF BUS SERVICES', 'NUMBER OF RAILWAY SERVICES',  'NUMBER NAVIGABLE WATERWAYS/CANALS', 'NUMBER OF CINEMA/VIDEO HALLS', 'NUMBER OF SPORTS CLUBS']

df_fin = pd.DataFrame()

inds = [[42,44], [48,50], [70, 72, 77, 79, 84, 86, 91, 93, 98, 100, 105, 107, 112, 114, 119, 121], [162], [138], [150], [252], [261], [271,273], [275], [309], [343], [345]]

dhcb_path = argv[1]
sum = 0


for fl in os.listdir(dhcb_path):

	try:

		fnd = len(fl) - fl[::-1].find('_')
		df = pd.read_excel(os.path.join(dhcb_path,fl), sheet_name=None)['Village_Data_{}'.format(fl[fnd:fnd+4])]

		print("Filename:", fl)

		print("The columns are:")
		for ind_list in inds:
			lst = []
			for col in ind_list:
				lst += [df.columns[col]]

			print(lst)

		# Replace null values with 0		
		for i in range(len(df.columns)):
			df.loc[df.iloc[:,i].isnull(), df.columns[i]] = 0

		for i in range(len(inds)):
			ind_list = inds[i]
			if len(ind_list) > 1:
				if i == 8:
					df.iloc[:,271] += df.iloc[:,273]
					df.loc[df.iloc[:,271] == 4, df.columns[271]] = 0
					df.loc[(df.iloc[:,271] == 1) | (df.iloc[:,271] == 2) | (df.iloc[:,271]==3), df.columns[271]] = 1
				elif i < 6:
					first = ind_list[0]
					for j in ind_list:
						if first == j:
							continue
						df.iloc[:,first] += df.iloc[:,j]
			else:
				if i >= 6:
					col = ind_list[0]
					df.loc[df.iloc[:,col] == 2, df.columns[col]] = 0
					
			
		col_list = ['Village Code']
		for ind_list in inds:
			col_list += [df.columns[ind_list[0]]]

		
		print("Number of rows in current df = {}".format(len(df)))
		print()
		print()
		sum += len(df)	

	except:
		print("Error found...")
		print()
		print()
		continue

	df_fin = df_fin.append(df[col_list], ignore_index=True)

print("Total number of supposed rows:", sum)
print("Total number of rows in final df:", len(df_fin))

import pickle
pickle.dump(df_fin, open('2011_input_dataframe.pickle', 'wb'))
	
		



