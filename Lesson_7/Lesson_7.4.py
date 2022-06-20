import os
import sys
folder_stat = {}
def scan_mem(pth):
    if not os.path.exists(pth):
        return
    with os.scandir(pth) as files:
        for node in files:
            if os.path.isfile(node):
                x = 10 ** len(str(os.stat(node).st_size))
                folder_stat[x] = folder_stat.get(x, 0) + 1
            elif os.path.isdir(node):
                scan_mem(os.path.join(pth, node))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        pth = sys.argv[1]
        print(pth)
    else:
        pth = os.getcwd()
    scan_mem(pth)
    print(folder_stat)