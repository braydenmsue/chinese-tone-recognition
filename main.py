import os
import sys
import wave
import numpy as np
from AudioHandler import AudioHandler
from ToneHandler import ToneHandler
import matplotlib.pyplot as plt
import librosa
import librosa.display


def format_input(input_dir):
    filepath = os.path.join(os.getcwd(), 'Recordings', input_dir)
    filenames = os.listdir(filepath)
    filenames = [os.path.join(filepath, f) for f in filenames]

    return filenames


def main(input_dir):
    filenames = format_input(input_dir)

    AH = AudioHandler()
    AH.process_audio(filenames)
    # AH.information()

    TH = ToneHandler(AH)

    i = 0
    for word in AH.word_array:
        AH.play_word(i)
        i += 1  # increment index to play next word

        print(" WORD ", i)
        f0, times = TH.f0_over_time(word)

        plt.figure(figsize=(10, 6))
        plt.plot(times, f0, label="Fundamental Frequency (F0)", color="blue")
        plt.xlabel("Time (s)")
        plt.ylabel("Frequency (Hz)")
        plt.title("Fundamental Frequency Over Time")
        plt.ylim(0, 500)
        plt.legend()
        plt.grid()
        plt.show()

    return


if __name__ == "__main__":
    main(sys.argv[1])
