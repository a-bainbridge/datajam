import math
import itertools
import playchords
import config

BITS_PER_CHORD = math.floor(math.log(len(config.CHORDS), 2))

def encode(stringinput):
    CHORDS_LIST=[]
    binlist=''
    for c in list(stringinput):
        binlist+=(format(ord(c),'07b'))
    for i in range(0,len(binlist),2):
        CHORDS_LIST.append(config.CHORDS[int(binlist[i:i+2],2)])
    return CHORDS_LIST

def cleanup(ear):
    clean=[]
    last='no match'
    andbefore='no match'
    for heard in ear:
        if not(heard=='no match'):
            if not(heard==last):
                clean.append(heard)
            elif heard==andbefore:
                clean.append(heard)
        andbefore=last
        last=heard
    return clean

def decode(chord_indices):
    binlist=''
    for i in chord_indices:
        binlist+=format(i,'02b')
    decoded=''
    for i in range(0,len(binlist),7):
        decoded+=chr(int(binlist[i:i+7],2))
    return decoded

if __name__ == "__main__":  
    CHORDS_LIST = []
    CHORDS_MAP = {}
    i = 0
    for j in itertools.product(range(2), repeat=BITS_PER_CHORD):
        CHORDS_MAP[j] = config.CHORDS[i]
        i += 1
    encode("inputtext.txt")
    playchords.play_chords(CHORDS_LIST)
