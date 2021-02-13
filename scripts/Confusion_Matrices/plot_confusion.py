import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torchvision
from torch.autograd import Variable
from torchvision import datasets, models, transforms
import os
import numpy as np
from trainloop import RunManager,RunBuilder
from collections import OrderedDict
from tqdm import tqdm
from sys import argv
import time

#torch.nn.Module.dump_patches = True

model_name = argv[1]
data_dir = argv[2]
data_type = 'val'
filename = argv[3]

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

data_transforms = {
    'train': transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485,0.456,0.406] , [0.229,0.224,0.225])
    ]),
    'val': transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485,0.456,0.406] , [0.229,0.224,0.225])
    ])
}

image_dataset = datasets.ImageFolder(os.path.join(data_dir,data_type),data_transforms[data_type])

model = torch.load(model_name,map_location = device)
model.train()

b_size = 50
do_shuffle = True

dataloader = torch.utils.data.DataLoader(image_dataset, batch_size = b_size,
                                                shuffle = do_shuffle, num_workers = 8)


conf = np.zeros((3,3))
batch = 0

if torch.cuda.is_available():
    print("cuda is available", device)
    print(torch.cuda.get_device_name(0))


try:
    for images, labels in dataloader:

        batch += 1
        start = time.time()

        images = Variable(images)
        labels = Variable(labels)

        if torch.cuda.is_available():
            images = images.cuda()
            labels = labels.cuda()

        output = model(images)

        _, preds = torch.max(output, 1)

        # labels, preds = labels.cpu(), preds.cpu()
        for i in range(preds.size()[0]):
            # print(images.size(), preds.size())
            conf[labels[i], preds[i]] += 1

        end = time.time()

        print("Batch {} completed.".format(batch))
        print("Time taken: {} minutes".format((end-start)/60.0))
        print()

except:
    print("Error found, thus rest of images skipped.".format(batch))

import pickle
f = open('./matrices/{}.pickle'.format(filename), 'wb')
pickle.dump(conf, f)
print("Matrix created!")
print(conf)
