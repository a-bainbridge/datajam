import math
import itertools
import playchords
import config

BITS_PER_CHORD = math.floor(math.log(len(config.CHORDS), 2))

def encode(infn):
    stringinput = ""
    with open(infn, "r") as f:
        for c in itertools.chain.from_iterable(f):
            stringinput += "{0:b}".format(ord(c));
    for i in range(0, len(stringinput), BITS_PER_CHORD):
        stringlist = list(stringinput[i:i+BITS_PER_CHORD])
        intlist = [int(k) for k in stringlist]
        if len(intlist) < 3:
            intlist = intlist + [0] * (BITS_PER_CHORD - len(intlist))
        CHORDS_LIST.append(CHORDS_MAP[tuple(intlist)])


if __name__ == "__main__":  
    CHORDS_LIST = []
    CHORDS_MAP = {}
    i = 0
    for j in itertools.product(range(2), repeat=BITS_PER_CHORD):
        CHORDS_MAP[j] = config.CHORDS[i]
        i += 1
    encode("inputtext.txt")
    playchords.play_chords(CHORDS_LIST)
