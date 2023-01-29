from math import floor, ceil
import numpy as np
import simpleaudio as sa
import random
scale = ["SP", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
CHORDS = [["C4", "E4", "G4"],["C4", "G4", "B4"],["B4","D4","F4"], ["A4", "F4", "C5"]]
frequencies = {
  "SP": 0.00,
  "C4": 261.63,
  "D4": 293.66,
  "E4": 329.63,
  "F4": 349.23,
  "G4": 392.00,
  "A4": 440.00,
  "B4": 493.88,
  "C5": 523.25
}
# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 0.20
samples = T/(1/44100)
if int(samples) != samples:
  print("fucked up")
samples = round(samples)
t = np.linspace(0, T, samples, False)

windowing = np.ones(samples)
windowing_start = 0.5

windowing[ceil(samples*windowing_start):] = np.linspace(1,0,floor(samples*(1-windowing_start)), False)

NOTES = {}
for name, frequency in frequencies.items():
  NOTES[name] = np.sin(float(frequency) * t * 2 * np.pi) * windowing

def play_chords(track: list[list[str]]):
  audio = np.zeros(round(44100 * len(track) * T))
  offset = 0
  for note_list in track:
    for note in note_list:
      audio[0 + offset: samples + offset] += NOTES[note]
    max_amplitude = np.max(np.abs(audio[0 + offset: samples + offset]))
    if max_amplitude > 0.00001:
      audio[0 + offset: samples + offset] *= 32767 / max_amplitude
    offset += samples
  # convert to 16-bit data
  audio = audio.astype(np.int16)
  # start playback
  play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
  # wait for playback to finish before exiting
  play_obj.wait_done()

if __name__ == "__main__":
  aha = random.choices(range(len(CHORDS)), k=100)
  track = [CHORDS[i] for i in aha]
  play_chords(track)