import sys
sys.path.insert(0, "/home/mongropython/.local/lib/python3.12/site-packages")

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    for elem in ft_tqdm(range(1000)):
        sleep(0.005)
    print()
    for elem in tqdm(range(1000)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
