import texttochords
import fileinput
import config

LIST_OF_INDECES = ['1', '2', '1', '0']

with open("output.txt", "w") as f:
    stringbin = ""
    for i in LIST_OF_INDECES:
        inttuple = config.CHORDS[LIST_OF_INDECES[i]]
        stringtuple = [tuple(str(x) for x in tup) for tup in inttuple]
        
        for 
        
if __name__ == "__main__":
    f.write(CHORDS_MAP)