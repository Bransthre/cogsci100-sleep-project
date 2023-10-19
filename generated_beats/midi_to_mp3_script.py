import os
from pydub import AudioSegment

def midi_to_mp3(midi_file, soundfont, mp3_file):
    wav_file = mp3_file.replace('.mp3', '.wav')
    os.system(f'fluidsynth -ni {soundfont} {midi_file} -F {wav_file} -r 44100')
    audio = AudioSegment.from_wav(wav_file)
    audio.export(mp3_file, format='mp3')
    os.remove(wav_file)


all_midi_sources = [
    f'./midi_sources/{file_name}'
    for file_name in os.listdir("./midi_sources")
]
soundfont_addr = "/usr/share/sounds/sf2/default-GM.sf2"
all_mp3_names = [
    file_name.replace(".midi", ".mp3").replace("midi_sources", "compiled_mp3")
    for file_name in all_midi_sources
]

for midi_file, mp3_file in zip(all_midi_sources, all_mp3_names):
    midi_to_mp3(midi_file, soundfont_addr, mp3_file)
