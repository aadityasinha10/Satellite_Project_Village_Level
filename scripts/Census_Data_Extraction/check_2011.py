import pandas as pd

inds = [[42,44], [48,50], [70, 72, 77, 79, 84, 86, 91, 93, 98, 100, 105, 107, 112, 114, 119, 121]]

df = pd.read_excel('../2011_Census_DCHB/DCHB_Village_Release_0700.xlsx')

# print(type(2) == type(5))
# print(type('x') == type(2))
# print(df.dtypes[42])


# for i in range(len(df)):
# 	if type(2) != type(df.iloc[i,42]):
# 		print(df.iloc[i,42])
# 		print(i)

# print(df.columns[42])


for i in range(len(inds)):
	ind_list = inds[i]
	first = ind_list[0]
	for j in ind_list:
		if first == j:
			continue
		df.iloc[:,first] += df.iloc[:,j]

	print(i)

