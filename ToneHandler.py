from AudioHandler import AudioHandler
import noisereduce as nr
import numpy as np
import librosa


class ToneHandler:
    def __init__(self, AH: AudioHandler):
        self.raw_data = AH.word_array
        self.sample_width = AH.sample_width
        self.channels = AH.channels
        self.frame_rate = AH.frame_rate

    # TODO: try ML model to predict tone (need dataset w/ words and expected tones)

    def get_tone(self, word_f0, threshold=50):

        start, end, global_max, global_min = self.f0_info(word_f0)
        print("------------------------")
        print("START Hz: ", start)
        print("END Hz: ", end)
        print("MAX Hz: ", global_max)
        print("MIN Hz: ", global_min)
        print("------------------------")

        # scaling threshold based on range of f0 values
        hz_range = abs(global_max - global_min)
        if hz_range > threshold * 1.5:  # arbitrary scaling factor
            print("OLD THRESHOLD:", threshold)
            threshold = hz_range * 0.5  # arbitrary scaling factor
            print("NEW THRESHOLD:", threshold)

        # if starts and ends in same place; range is small (tone is consistent)
        if abs(end - start) < threshold and abs(global_max - global_min) < threshold:
            print("Tone: 1")
        # if max is near the end and min is near the start
        elif abs(global_max - end) < threshold and abs(global_min - start) < threshold:
            print("Tone: 2")
        # start and end are close, but range is large
        elif abs(end - start) < threshold < hz_range:
            print("Tone: 3")
        elif start > global_min and end > global_min:
            print("Tone: 3 (LESS CERTAIN)")
        elif abs(global_max - start) < threshold and abs(global_min - end) < threshold:
            print("Tone: 4")
        else:
            print("DON'T KNOW")

        print("\n")


    def f0_info(self, f0_array):
        # returns start, end, global_max, global_min

        f0_cleaned = f0_array[~np.isnan(f0_array)]

        return f0_cleaned[0], f0_cleaned[-1], np.max(f0_cleaned), np.min(f0_cleaned)

    def f0_over_time(self, word):
        filtered_word = self.reduce_noise(word)
        f0, voiced_flag, voiced_probs = librosa.pyin(filtered_word, fmin=50, fmax=400, sr=self.frame_rate)
        times = librosa.times_like(f0, sr=self.frame_rate)
        self.get_tone(f0)

        return f0, times

    def reduce_noise(self, word):
        word_filtered = nr.reduce_noise(y=word, sr=self.frame_rate)
        word_trimmed = librosa.effects.trim(word_filtered, top_db=10)[0]
        return word_trimmed
