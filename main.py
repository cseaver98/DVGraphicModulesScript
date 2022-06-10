import tkinter as tk
import re
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

targetStr = 'DVSYS.'
index = 0
lineIndex = 0
set = set()

# opening a text file
filename = filedialog.askopenfilename()

with open(filename, 'r', errors='ignore') as file:
    for line in file:
        index += 1

        if targetStr in line:
            words = re.split(targetStr, line)

            for index1, word in enumerate(words):
                if index1 == 0:
                    continue
                temp = 0
                for index2, chr in enumerate(word):
                    if not re.match(r'^[A-Za-z0-9_]+$', chr):
                        temp = index2
                        break
                if len(word[0:temp]) > 3 and not word[0:temp].isalpha():
                    if word[0:temp][-1].isdigit() or word[0:temp][-1].isalnum():
                        # print(word[0:temp], index)
                        set.add(word[0:temp])
                    else:
                        # print(word[0:temp-1], index)
                        set.add(word[0:temp-1])
with open(filename[0:len(filename)-4] + '_modules.txt', 'w') as f:
    for elem in set:
        f.write(elem+"\n")



