import numpy as np

x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"

def reverse_test(x):
    pages = []
    lines = []
    words = []

    index = 0
    for i in np.arange(len(x)):
        if x[i:i+1] == "\b":
            pages.append(x[index:i])
            index = i+1

    for i in np.arange(len(pages)):
        index = 0
        for j in np.arange(len(pages[i])):
            if pages[i][j:j+1] == "\n":
                lines.append(pages[i][index:j])
                index = j+1

            
    for i in np.arange(len(lines)):
        index = 0
        for j in np.arange(len(lines[i])):
            if lines[i][j:j+1] == " ":
                words.append(lines[i][index:j])
                index = j+1
        words.append(lines[i][index:])
    words = np.flip(words)
            
            
    print("words = ", words)



reverse_test(x)
