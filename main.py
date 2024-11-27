import os
import sys
import wave
import numpy as np
from AudioHandler import AudioHandler


def format_input(input_dir):
    filepath = os.path.join(os.getcwd(), 'Recordings', input_dir)
    filenames = os.listdir(filepath)
    filenames = [os.path.join(filepath, f) for f in filenames]

    return filenames


def main(input_dir):
    filenames = format_input(input_dir)

    AH = AudioHandler()
    AH.process_audio(filenames)
    print(filenames)
    AH.information()
    words = AH.get_words()

    for i in range(len(AH.get_words())):
        word = AH.get_word(i)
        AH.play_audio(word)


    return


if __name__ == "__main__":
    main(sys.argv[1])
