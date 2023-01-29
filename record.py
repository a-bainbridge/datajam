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
    d=0
    e=0
    f=0
    di=0
    ei=0
    fi=0
    i=5

    while i<len(x):
        if xf[i]>250 and xf[i]<550:
            if x[i]>a:
                fi=ei
                f=e
                ei=di
                e=d
                di=ci
                d=c
                ci=bi
                c=b
                bi=ai
                b=a
                ai=i
                a=x[i]
            elif x[i]>b:
                fi=ei
                f=e
                ei=di
                e=d
                di=ci
                d=c
                ci=bi
                c=b
                bi=i
                b=x[i]
            elif x[i]>c:
                fi=ei
                f=e
                ei=di
                e=d
                di=ci
                d=c
                ci=i
                c=x[i]
            elif x[i]>d:
                fi=ei
                f=e
                ei=di
                e=d
                di=i
                d=x[i]
            elif x[i]>e:
                fi=ei
                f=e
                ei=i
                e=x[i]
            elif x[i]>f:
                fi=i
                f=x[i]
        i+=1

    return [ai,bi,ci,di,ei,fi]

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

audio=audio[-4096:]
n=len(audio)
yf = fft(audio)
xf = fftfreq(n,1./float(config.SAMPLE_RATE))*.363
#peakindices, garbage = find_peaks(yf[:int(n/2)],height=600000)
freqs = xf[checkfreq(np.abs(yf)[:int(n/2)])]
print(freqs)
notes = freqtonotes(freqs)

try:
    print(config.CHORDS.index(notes))
except:
    print("no chord :(")
from matplotlib import pyplot
pyplot.plot(xf[:int(n/2)],np.abs(yf)[:int(n/2)]) #magic 2
pyplot.xlim([0,2000])
pyplot.show()
