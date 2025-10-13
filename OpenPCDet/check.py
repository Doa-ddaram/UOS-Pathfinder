import numpy as np

for i in range(1000, 10000):
    data = np.load(f"data/custom_av/points/1010{i}.npy")
    if data.shape[1] != 4:
        print('not shape 4')