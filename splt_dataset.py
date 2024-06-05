import os
import glob
import csv
import random

def get_images(path):
    return glob.glob(path+'\\**\\*.jpg', recursive=True) + glob.glob(path+'\\*.png', recursive=True)

onca = get_images("C:\\Users\\Augusto\\Desktop\\Trabalhomc906\\dataset\\onca")
peru = get_images("C:\\Users\\Augusto\\Desktop\\Trabalhomc906\\dataset\\peru")
guaxinim = get_images("C:\\Users\\Augusto\\Desktop\\Trabalhomc906\\dataset\\guaxinim")
background = get_images("C:\\Users\\Augusto\\Desktop\\Trabalhomc906\\dataset\\background")

o = len(onca)
o = int(o*.8)
p = len(peru)
p = int(p*.8)
g = len(guaxinim)
g = int(g*.8)
b = len(background)
b = int(b*.8)


random.shuffle(onca)
random.shuffle(peru)
random.shuffle(guaxinim)
random.shuffle(background)

print(o,p,g,b)

t_o = onca[:o]
v_o = onca[o:]

t_p = peru[:p]
v_p = peru[p:]

t_g = guaxinim[:g]
v_g = guaxinim[g:]

t_b = background[:b]
v_b = background[b:]

train = t_g + t_o + t_p + t_b
val = v_g + v_p + v_o + v_b
y = 0
for i in train:
    for j in val:
        if i == j :
            print(i)
            print(j)
            print()
print(y)

with open('train.txt','w') as file:
    for i in train:
        file.write(i+'\n')

with open('val.txt','w') as f:
    for i in val:
        f.write(i+'\n')
