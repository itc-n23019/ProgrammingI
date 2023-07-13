import pickle

with open('test1.pk1', 'wb') as f:
    my_list = list(range(1, 11))
    pickle.dump(my_list , f)
import pickle
with open('test1.pk1', 'rb') as f:
    my_list = pickle.load(f)
    print(my_list)
"""
import pickle

try:
    with open('test1.pk1', 'r') as f:
        my_list = pickle.load(f)
except FileNotFoundError:
    my_list = list(range(1, 11))
    with open('test1.pk1', 'w') as f:
        pickle.dump(my_list, f)

import pickle
import os

file_path = 'test1.pk1'

if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        my_list = pickle.load(f)
else:
    my_list = list(range(1, 11))
    with open(file_path, 'wb') as f:
        pickle.dump(my_list, f)

print(my_list)
"""
