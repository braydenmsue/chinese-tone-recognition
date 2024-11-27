import os
import wave
import pyaudio
import numpy as np
from pydub import AudioSegment


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
        if filename_array is None:
            print("ERROR: Input filename array is empty.")
            return []

        first_word = AudioSegment.from_file(file=filename_array[0], format="wav")
        self.frame_rate = first_word.frame_rate
        self.channels = first_word.channels
        self.sample_width = first_word.sample_width

        self.word_array.append(first_word)
        for f in filename_array[1:]:
            self.word_array.append(AudioSegment.from_file(file=f, format="wav"))

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


    def get_words(self):
        """
        Returns the list of AudioSegment objects representing each word.

        Returns:
            list: List of AudioSegment objects
        """
        return self.word_array

    def get_word(self, i):
        """
        Returns a specific word (AudioSegment) from the word array.

        Args:
            i (int): Index of the word to return.

        Returns:
            AudioSegment: The word at the specified index.
        """
        return self.word_array[i]

    def play_audio(self, audio_segment):
        """
        Plays the given AudioSegment using pyaudio.

        Args:
            audio_segment (AudioSegment): The AudioSegment to play.

        Returns:
            None
        """
        # Convert AudioSegment to raw audio data
        raw_data = audio_segment.raw_data

        # Initialize PyAudio stream
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(self.sample_width),
                        channels=self.channels,
                        rate=self.frame_rate,
                        output=True)

        # Play the audio data in chunks
        chunk_size = 1024
        for i in range(0, len(raw_data), chunk_size):
            chunk = raw_data[i:i + chunk_size]
            stream.write(chunk)

        # Close the stream and terminate PyAudio
        stream.stop_stream()
        stream.close()
        p.terminate()
