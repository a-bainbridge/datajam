from math import floor, ceil
import numpy as np
import simpleaudio as sa
import random
import config
# get timesteps for each sample, T is note duration in seconds

samples = config.NOTE_DURATION * config.SAMPLE_RATE
if int(samples) != samples:
  print("uh oh")
samples = round(samples)
t = np.linspace(0, config.NOTE_DURATION, samples, False)

windowing = np.ones(samples)
windowing_start = 0.95

windowing[ceil(samples*windowing_start):] = np.linspace(1,0,floor(samples*(1-windowing_start)), False)

notes_data = {}
for name, frequency in config.FREQUENCIES.items():
  notes_data[name] = np.sin(float(frequency) * t * 2 * np.pi) * windowing

def play_chords(track: list[list[str]]):
  audio = np.zeros(round(config.SAMPLE_RATE * len(track) * config.NOTE_DURATION))
  offset = 0
  for note_list in track:
    for note in note_list:
      audio[0 + offset: samples + offset] += notes_data[note]
    max_amplitude = np.max(np.abs(audio[0 + offset: samples + offset]))
    if max_amplitude > 0.00001:
      audio[0 + offset: samples + offset] *= 32767 / max_amplitude
    offset += samples
  # convert to 16-bit data
  audio = audio.astype(np.int16)
  # start playback
  play_obj = sa.play_buffer(audio, 1, 2, config.SAMPLE_RATE)
  # wait for playback to finish before exiting
  play_obj.wait_done()

if __name__ == "__main__":
  aha = random.choices(range(len(config.CHORDS)), k=10)
  #aha = [2] 
  track = [config.CHORDS[i] for i in aha]
  play_chords(track)
