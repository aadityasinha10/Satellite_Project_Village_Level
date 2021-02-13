import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import torch 
torch.multiprocessing.set_sharing_strategy('file_system')
import torch.nn as nn
import torchvision
#import datasets in torchvision
import torchvision.datasets as datasets

#import model zoo in torchvision
import torchvision.models as models
import torchvision.transforms as transforms

import os
from skimage import io, transform
import sys

img_transform = transforms.Compose([
    # transforms.Resize(224),
    transforms.ToTensor(),
    #normalize the images with imagenet data mean and std
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

filename_list = []
IMAGE_DIR = sys.argv[1]

for dr in os.listdir(IMAGE_DIR):
	for fl in os.listdir(os.path.join(IMAGE_DIR,dr)):
		filename_list += [dr+'/'+fl]

print("Hello")

print(len(filename_list))

class IDataset:

	def __init__(self, img_dir, name_list):

		self.img_dir = img_dir
		self.name_list = name_list

	def __len__(self):
		return len(self.name_list)

	def __getitem__(self, idx):

		vill_rev = self.name_list[idx][::-1]
		dot = vill_rev.find('.')
		at = vill_rev.find('@')
		vill_id = int((vill_rev[dot+1:at])[::-1])
		
		img_name = os.path.join(self.img_dir, self.name_list[idx])
		image = io.imread(img_name)
		image = img_transform(image)

		sample = {'image': image, 'vill_id': vill_id}
		return sample




from torch.utils.data import Dataset, DataLoader

train_dataset = IDataset(
	IMAGE_DIR, filename_list)

BATCH_SIZE = 50
NUM_WORKERS = 8

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = torch.load(sys.argv[3], map_location=device)
model.eval()


out_dict = {}
out_path = sys.argv[2]


for sample in train_loader:
	images, vill_ids = sample['image'], sample['vill_id']

	if torch.cuda.is_available():
		images = images.cuda()
	
	outputs = model(images)

	for i in range(vill_ids.size(0)):
		lst = outputs[i].tolist()
		temp = lst[0]
		lst[0] = lst[2]
		lst[2] = temp

		out_dict[int(vill_ids[i])] = lst
		


	
print("Done and dusted!")

import pickle
pickle.dump(out_dict, open(out_path, 'wb'))

	



	

