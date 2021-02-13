import pandas as pd
from sys import argv
import os

columns = ['VILLAGE CODE','NUMBER OF PRIMARY SCHOOLS', 'NUMBER OF MIDDLE SCHOOLS', 'NUMBER OF COLLEGES', 'NUMBER OF ALLOPATHIC HOSPITALS', 'NUMBER OF MATERNITY AND CHILD WELFARE CENTRES', 'NUMBER OF PRIMARY HEALTH CENTER', 'NUMBER OF POST OFFICES', 'NUMBER OF TELEPHONE CONNECTIONS', 'NUMBER OF BUS SERVICES', 'NUMBER OF RAILWAY SERVICES',  'NUMBER NAVIGABLE WATERWAYS/CANALS', 'NUMBER OF CINEMA/VIDEO HALLS', 'NUMBER OF SPORTS CLUBS']

df_fin = pd.DataFrame()

inds = [[42,44], [48,50], [70, 72, 77, 79, 84, 86, 91, 93, 98, 100, 105, 107, 112, 114, 119, 121], [162], [138], [150], [252], [261], [271,273], [275], [309], [343], [345]]

dhcb_path = argv[1]
sum = 0
num_files = 0

for fl in os.listdir(dhcb_path):

	fnd = len(fl) - fl[::-1].find('_')
	df = pd.read_excel(os.path.join(dhcb_path,fl), sheet_name=None)['Village_Data_{}'.format(fl[fnd:fnd+4])]

	print("Filename:", fl)

	# Replace null values with 0		
	for lst in inds:
		for i in lst:
			sum += df.iloc[:,i].isnull().sum()

	num_files += 1


num_cols = 0
for lst in inds:
	for ind in lst:
		num_cols += 1


print("Total null values:", sum)
print("Average null values per column:", sum/(num_cols))
	
		



