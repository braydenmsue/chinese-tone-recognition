from AudioHandler import AudioHandler


class ToneHandler:
    def __init__(self, AH: AudioHandler):
        self.data = self.get_sound_data(AH.get_words())
        self.sample_width = AH.sample_width
        self.channels = AH.channels
        self.frame_rate = AH.frame_rate

    @staticmethod
    def get_sound_data(words):
        raw_data = []
        for word in words:
            raw_data.append(word.raw_data)
        return raw_data
