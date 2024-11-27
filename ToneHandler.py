from AudioHandler import AudioHandler


class ToneHandler:
    def __init__(self, AH: AudioHandler):
        self.data = AH.word_array
        self.sample_width = AH.sample_width
        self.channels = AH.channels
        self.frame_rate = AH.frame_rate

