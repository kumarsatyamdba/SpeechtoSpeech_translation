import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

    
sound = AudioSegment.from_file("C:/Users/Asus/Desktop/mustc/es.mp3")
chunks = split_on_silence(sound, 
     # must be silent for at least half a second
min_silence_len=1000,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-30
)

for i, chunk in enumerate(chunks):
    chunk.export("C:/Users/Asus/Desktop/mustc/es_out/es_{0}.wav".format(i), format="wav") 

