import re
from os import path
from pydub import AudioSegment
from pydub.playback import play


class Model:
    def __init__(self, data=None):
        pass

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, value):
        pattern = r'\.wav$'  # Match file extension ".wav" at the end

        if re.fullmatch(pattern, value):
            self.__sound = value
        else:
            src = value
            dst = value.replace('.mp3', '.wav')

            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")

            raw_audio = AudioSegment.from_file(dst, format="wav")
            channel_count = raw_audio.channels
            print(channel_count)

            mono_wav = raw_audio.set_channels(1)
            mono_wav.export("pt_mono.wav", format="wav")

            mono_wav_audio = AudioSegment.from_file("pt_mono.wav", format="wav")
            channel_count = mono_wav_audio.channels
            print(channel_count)

    def save(self, input_file, output_file):
        audio = AudioSegment.from_file(input_file, format="wav")
        audio.export(output_file, format="wav")
