import sys
import os
import pickle

indi_path = sys.argv[1]
out_path = sys.argv[2]

count = 0
out_dict = {}
geo_dict = pickle.load(open('/home/cse/mtech/mcs192554/scratch/Geo_Info/vill_geoinfo.pickle', 'rb'))
ids = set()
repeated_ids = set()

for cluster in os.listdir(indi_path):
    for vill in os.listdir(os.path.join(indi_path, cluster)):
        vill_rev = vill[::-1]
        dot = vill_rev.find('.')
        at = vill_rev.find('@')
        vill_id = int((vill_rev[dot+1:at])[::-1])
        count += 1

        out_dict[vill_id] = geo_dict[vill_id]

        if vill_id in ids:
            repeated_ids.add(vill_id)
        else:
            ids.add(vill_id)


print("\nTotal number of villages for this indicator is:", count)
print("Total #keys in the out dict is:", len(out_dict))
print("Total number of repeated ids is:", len(repeated_ids))

pickle.dump(out_dict, open(os.path.join(out_path,'fc_ids'), 'wb'))
