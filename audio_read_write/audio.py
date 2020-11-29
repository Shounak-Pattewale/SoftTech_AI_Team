######### Basic Information #########

# 1 khz = 1000 pieces of info per sec
# Freq (Hz) = length of wave boject array/duration of audio file (sec)
# OR
# Duration of audio file (sec) = length of wave object array/frequency (Hz)
# https://github.com/jiaaro/pydub

import wave
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
# import PyAudio

song_mp3 = AudioSegment.from_mp3("audio_files/down_mp3.mp3")
# Use 'from_ogg' for oga and ogg
# Use 'from_mp3' for mpeg and mp3

song_mp3.export("audio_files/down_mp3_to_wav.wav",format="wav")
filepath = "audio_files/down_mp3_to_wav.wav"

######### To read an audio file #########

def audio_reading(filepath):
    wav = wave.open(filepath,"r")

    soundwave_wav = wav.readframes(-1)
    data_wav = np.frombuffer(soundwave_wav,np.int16)
    print("data_wav : ",data_wav)

    ######### To write data into text file #########

    # file = open('audio.txt', 'w')
    # for d in data_wav:
    #     file.write(str(d))
    #     # print(d)
    # file.close()

    channels = wav.getnchannels()           # Channels i.e mono, sterio, etc
    print("Channels : ",channels)

    sRate_wav = wav.getframerate()          # Sampling Frequency, i.e frames per sec
    print("Frame Rate (Sampling freq) : ",sRate_wav)

    nFrames_wav = wav.getnframes()          # Total no of frames
    print("Total no of Frames : ",nFrames_wav)

    width_wave = wav.getsampwidth()         # Sample width(bytes) i.e one sample is stored in these many bytes
    print("Sampling width : ",width_wave)

    data_wav.shape = -1,channels
    print("data_wav Shape : ",data_wav.shape)
    # print(data_wav)

    data_wav = data_wav.T
    # print(data_wav)

    timeDuration_wav = nFrames_wav/float(sRate_wav)
    print("Total audio length (sec) : ",timeDuration_wav)

    duration = 1/float(sRate_wav)
    print("Duration : ",duration)

    # timeSeq_wav = np.linspace(start=0,stop=len(data_wav)/sRate_wav,num=len(data_wav))

    timeSeq = np.arange(0,timeDuration_wav,duration)
    print("Time Sequence : ",timeSeq)

    ######### To generate graph (channel wise) #########

    # plt.title("Audio File")
    # plt.xlabel("Time (sec)")
    # plt.ylabel("Amplitude")

    # plt.plot(timeSeq,data_wav[0],label="Audio Graph")
    # plt.legend()
    # plt.show()
    # plt.savefig('audio_graphs/audio.png', transparent=True, bbox_inches='tight')

audio_reading(filepath)


######### For writing an audio file #########

# file = "audio_files/test_wav.wav"
file = filepath

def audio_writing(file):

    song = AudioSegment.from_wav(file)
    backwards = song.reverse()
    backwards.export("audio_files/reverse_down.wav",format="wav")
    ten_seconds = 10 * 1000
    first_10_seconds = song[:ten_seconds]
    # last_5_seconds = song[-5000:]
    first_10_seconds.export("audio_files/10sec_down.wav",format="wav")

audio_writing(file)