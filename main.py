# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import shutil

if __name__ == "__main__":

    path = "I:\Bao\假类含挑选和非挑选\Prada\\sign\\sign_2"
    path_need = path+"_need"
    files_need = os.listdir(path_need)
    files_all = os.listdir(path)
    n = 0
    for file in files_need:
        if file in files_all:
            os.remove(os.path.join(path, file))
            n += 1
    print(n)

    os.rename(path, path+"_not")




