import glob
import os
import random
import shutil

def get_images(path):
    return glob.glob(path+'\\**\\*.jpg', recursive=True) + glob.glob(path+'\\*.png', recursive=True)


imgs = get_images("C:\\Users\\Augusto\\Desktop\\Trabalhomc906\\dataset\\background")

for i  in imgs:
    with open(i[:-3]+'txt','w') as file:
        pass
