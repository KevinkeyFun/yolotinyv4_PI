import os
files = os.listdir("/Users/kevin/Downloads/yolotinyv4_PI/train")
for src in files:
    dst = src.replace('.rf.', 'S2')
    os.rename(src, dst)

