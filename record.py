from pvrecorder import PvRecorder
from matplotlib import pyplot
from scipy.fft import fft, fftfreq

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
pyplot.plot(audio[:]) #8192
pyplot.show()
