from pvrecorder import PvRecorder
from scipy.fft import fft, fftfreq
#from scipy.signal import find_peaks
import numpy as np
import config

def otherfreqcheck(x):
    peak=[]
    for i in range(len(x)):
        if x[i]>250000:
            peak.append(i)
    return peak

def freqtonotes(f):
    #list of arrays to list of note names

    dnote=[]
    for note in config.FREQUENCIES:
        for freq in f:
            if np.abs(config.FREQUENCIES[note]-freq)<10 and not(note in dnote):
                dnote.append(note)
    return dnote

def listolistonotes2indices(l):
    #for testing the encoding/decoding setup

    i=[]
    for ch in l:
        i.append(config.CHORDS.index(ch))
    return i

def listen():
    n=4096
    rec = PvRecorder(device_index=-1,frame_length=n)
    notes=[]
    silencetime=101
    s=20

    rec.start()
    recording=True
    while silencetime<s or silencetime>100:
        frame=rec.read()
        yf=fft(frame)
        xf=fftfreq(n,1./float(config.SAMPLE_RATE))*.363
        freqs = xf[otherfreqcheck(np.abs(yf)[:int(n/2)])]
        try:
            notes.append(config.CHORDS.index(freqtonotes(freqs)))
            print(config.CHORDS.index(freqtonotes(freqs)))
            silencetime=0
        except:
            notes.append("no match")
            print("no match")
            silencetime+=1
    rec.stop()
    rec.delete()

    return(notes[:-s])
