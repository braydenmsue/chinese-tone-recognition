import numpy as np
import sounddevice as sd
import librosa


class AudioHandler:

    def __init__(self):
        self.word_array = []
        self.frame_rate = -1
        self.channels = -1
        self.sample_width = -1

    def process_audio(self, filename_array):
        """
        Populates AudioHandler object with data and metadata from audio files.

        Args:
            filename_array (list of str): List of paths to audio files.
                Each sentence is broken up into individual words and stored in a directory; all from same recording.

        Returns:
            None
        """
        if not filename_array:
            print("ERROR: Input filename array is empty.")
            return []

        # Load the first audio file to extract metadata
        first_word, sr = librosa.load(filename_array[0], sr=None, mono=True)  # Load the first word
        self.frame_rate = sr
        self.channels = 1  # Mono audio
        self.sample_width = np.dtype(first_word.dtype).itemsize  # Sample width in bytes, based on NumPy dtype

        # Append the first word's audio data to word_array
        self.word_array.append(first_word)

        # Process the rest of the files
        for f in filename_array[1:]:
            word_audio, _ = librosa.load(f, sr=self.frame_rate)  # Keep the same sample rate for all
            self.word_array.append(word_audio)

    def information(self):
        """
        Outputs and returns metadata of audio files.

        Returns:
            tuple: (frame_rate, channels, sample_width)
        """
        print("Frame rate: ", self.frame_rate)
        print("Channels: ", self.channels)
        print("Sample width: ", self.sample_width)
        return self.frame_rate, self.channels, self.sample_width

    def play_word(self, index):
        # Index specifies which word's audio to play from word_array
        audio_data = self.word_array[index]
        sd.play(audio_data, self.frame_rate)  # Play the audio at the original sample rate
        sd.wait()

    def play_words(self):
        for word in self.word_array:
            sd.play(word, self.frame_rate)
            sd.wait()
