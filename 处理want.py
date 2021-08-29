import shutil

import matplotlib.pyplot as plt
# import torch
import os

from tqdm import tqdm

if __name__ == "__main__":
    src = 'I:\KTB\images_want3'
    all_zfilled_images = sorted(os.listdir(src))
    pre = '/media/D_4TB/YL_4TB/Competitions/KTB/Code/runs/exp2_alltrain/input_data'
    # pre = '/media/D_4TB/YL_4TB/Competitions/KTB/Code/runs/exp2_alltrain/input_data'

    with open( 'I:\KTB\\train_want3.txt', 'w') as f:
        for zfilled_image in all_zfilled_images:
            sub, image = zfilled_image.split('_')
            sub = int(sub)
            path = pre +'/'+str(sub)+'/'+image
            # path = os.path.join(pre, str(sub), image)
            # print(path)
            f.write(path+'\n')


