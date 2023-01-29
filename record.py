from pvrecorder import PvRecorder
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks
import numpy as np
import config

def checkfreq(x):
    #returns top 3 indices of x

    a=0
    b=0
    c=0
    ai=0
    bi=0
    ci=0
    i=0

    while i<len(x):
        if x[i]>a:
            ci=bi
            c=b
            bi=ai
            b=a
            ai=i
            a=x[i]
            i+=5
        elif x[i]>b:
            ci=bi
            c=b
            bi=i
            b=x[i]
            i+=5
        elif x[i]>c:
            ci=i
            c=x[i]
            i+=5
        i+=1

    return [ai,bi,ci]


def freqtonotes(f):
    #list of arrays to list of note names

    dnote=[]
    for note in config.FREQUENCIES:
        for freq in f:
            if np.abs(config.FREQUENCIES[note]-freq)<10:
                dnote.append(note)
    return dnote

rec = PvRecorder(device_index=-1,frame_length=512)
audio=[]

rec.start()
recording=0
while recording<60:
    frame=rec.read()
    audio.extend(frame)
    #if audio[-1]==1: #to be replaced with the stop chord
    recording+=1
rec.stop()
rec.delete()

audio=audio[-8192:]
n=len(audio)
yf = fft(audio)
xf = fftfreq(n,1./float(config.SAMPLE_RATE))
#peakindices, garbage = find_peaks(yf[:int(n/2)],height=600000)
freqs = xf[checkfreq(np.abs(yf)[:int(n/2)])]*.363
print(freqs)
notes = freqtonotes(freqs)

from matplotlib import pyplot
pyplot.plot(xf[:int(n/2)]*.363,np.abs(yf)[:int(n/2)]) #magic 2
pyplot.xlim([0,2000])
pyplot.show()
print(config.CHORDS.index(notes))
