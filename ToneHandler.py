from AudioHandler import AudioHandler
import noisereduce as nr
import librosa


class ToneHandler:
    def __init__(self, AH: AudioHandler):
        self.raw_data = AH.word_array
        self.sample_width = AH.sample_width
        self.channels = AH.channels
        self.frame_rate = AH.frame_rate

    def f0_over_time(self, word):
        filtered_word = self.reduce_noise(word)
        f0, voiced_flag, voiced_probs = librosa.pyin(filtered_word, fmin=50, fmax=400, sr=self.frame_rate)
        times = librosa.times_like(f0, sr=self.frame_rate)

        return f0, times

    def reduce_noise(self, word):
        return nr.reduce_noise(y=word, sr=self.frame_rate)