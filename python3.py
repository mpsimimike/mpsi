#get folder

root = '/media/sf_Shared/Learn-Python/gmw'

import os

files = os.listdir(root)

txtlist = []

#append txt to list
for f in files:
    if f.endswith(".txt"):
        txtlist.append(f)

results = {}

#add to dict
for f in txtlist:
    results[f] = [item for item in f[:-4].split('_') if not item.isdigit()]



