#!/usr/bin/python
# -*- coding:utf-8 -*-
from glob import glob
from collections import defaultdict
import librosa
import numpy as np
from scipy.stats import pearsonr

# %%
import utils  # self-defined utils.py file

DB = 'GTZAN'
if DB == 'GTZAN':  # dataset with genre label classify at parent directory
    FILES = glob(DB + '/wav/*/*.wav')
    # print(FILES)
else:
    FILES = glob(DB + '/wav/*.wav')
    # print(FILES)

GENRE = [g.split('/')[2] for g in glob(DB + '/wav/*')]
print(GENRE)
n_fft = 100  # (ms)
hop_length = 25  # (ms)

# %% Q2
if DB == 'GTZAN':
    label, pred = defaultdict(list), defaultdict(list)
else:
    label, pred = list(), list()
chromagram = list()
gens = list()
for f in FILES:
    f = f.replace('\\', '/')
    print("file: ", f)
    content = utils.read_keyfile(f, '*.lerch.txt')
    if (int(content) < 0): continue  # skip saving if key not found
    if DB == 'GTZAN':
        gen = f.split('/')[2]
        label[gen].append(utils.LABEL[int(content)])
        gens.append(gen)
    else:
        label.append(utils.LABEL[content])

    sr, y = utils.read_wav(f)

    gamma = 1000
    # gamma = input("gamma (1, 10, 100, 1000): ")
    cxx = np.log(1 + gamma * np.abs(librosa.feature.chroma_stft(y=y, sr=sr)))
    chromagram.append(cxx)  # store into list for further use
    chroma_vector = np.sum(cxx, axis=1)
    key_ind = np.where(chroma_vector == np.amax(chroma_vector))
    key_ind = int(key_ind[0])
    # print('key index: ', key_ind)
    chroma_vector = utils.rotate(chroma_vector.tolist(), 12 - key_ind)
    # print('chroma_vector: ', chroma_vector)
    MODE = {"major": [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            "minor": [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]}
    r_co_major = pearsonr(chroma_vector, MODE["major"])
    r_co_minor = pearsonr(chroma_vector, MODE["minor"])
    # print(r_co_major[0])
    # print(r_co_minor[0])
    mode = ''
    if (r_co_major[0] > r_co_minor[0]):
        mode = key_ind
    else:
        mode = key_ind + 12
    mode = utils.lerch_to_str(mode)
    # print('mode', mode)
    if DB == 'GTZAN':
        pred[gen].append(mode)
    else:
        pred.append('?')  # you may ignore this when starting with GTZAN dataset
    # print(pred[gen])

print("***** Q2 *****")
if DB == 'GTZAN':
    label_list, pred_list = list(), list()
    print("Genre    \taccuracy")
    for g in GENRE:
        # TODO: Calculate the accuracy for each genre
        # Hint: Use label[g] and pred[g]
        correct = 0
        for acc_len in range(len(label[g])):
            if label[g][acc_len] == pred[g][acc_len]:
                correct += 1
        try:
            acc = correct / len(label[g])
        except ZeroDivisionError:
            acc = 0
        print("{:9s}\t{:8.2f}%".format(g, acc))
        label_list += label[g]
        pred_list += pred[g]
else:
    label_list = label
    pred_list = pred

# TODO: Calculate the accuracy for all file.
# Hint1: Use label_list and pred_list.
correct_all = 0
for acc_len in range(len(label_list)):
    if label_list[acc_len] == pred_list[acc_len]:
        correct_all += 1
try:
    acc_all = correct_all / len(label_list)
except ZeroDivisionError:
    acc_all = 0
##########
print("----------")
print("Overall accuracy:\t{:.2f}%".format(acc_all))

'''
GTZAN
***** Q2 *****
----------
gamma = 1

Genre    	accuracy
pop      	    0.40%
metal    	    0.22%
disco    	    0.33%
blues    	    0.07%
reggae   	    0.32%
classical	    -
rock     	    0.34%
hiphop   	    0.14%
country  	    0.34%
jazz     	    0.16%

Overall accuracy:	0.26%
----------
gamma = 10

Genre    	accuracy
pop      	    0.39%
metal    	    0.19%
disco    	    0.29%
blues    	    0.04%
reggae   	    0.29%
classical	    -
rock     	    0.31%
hiphop   	    0.15%
country  	    0.31%
jazz     	    0.11%

Overall accuracy:	0.24%
----------
gamma = 100

Genre    	accuracy
pop      	    0.34%
metal    	    0.19%
disco    	    0.29%
blues    	    0.04%
reggae   	    0.25%
classical	    -
rock     	    0.28%
hiphop   	    0.10%
country  	    0.31%
jazz     	    0.14%

Overall accuracy:	0.22%
----------
gamma = 1000

Genre    	accuracy
pop      	    0.33%
metal    	    0.19%
disco    	    0.28%
blues    	    0.05%
reggae   	    0.26%
classical	    -
rock     	    0.29%
hiphop   	    0.09%
country  	    0.31%
jazz     	    0.14%

Overall accuracy:	0.22%
----------
'''