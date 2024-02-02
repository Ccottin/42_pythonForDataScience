import sys
sys.path.insert(0, "/home/mongropython/.local/lib/python3.12/site-packages")

from time import sleep
#import time
from tqdm import tqdm
from Loading import ft_tqdm

#begin = time.time()
for elem in ft_tqdm(range(300)):
    sleep(0.005)
print()
#print(time.time() - begin)
#begin = time.time()
for elem in tqdm(range(300)):
    sleep(0.005)
print()
#print(time.time() - begin)

