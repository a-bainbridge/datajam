from pvrecorder import PvRecorder
from matplotlib import pyplot
from scipy.fft import fft, fftfreq
import numpy as np
import config

rec = PvRecorder(device_index=-1,frame_length=512)
audio=[]

rec.start()
recording=0
while recording<151:
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
pyplot.plot(xf[:int(n/2)],np.abs(yf)[:int(n/2)])
pyplot.show()
