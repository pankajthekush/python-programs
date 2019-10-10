
import speech_recognition as sr
import sys


class MappingLookup():
    #Mapping file to changee the words
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dictmapping = dict()



class ConvertToText():
    def __init__(self,audiofile):
        self.audiofile = audiofile
        self.returntext = []

    def convertotext(self):
        audiofile = self.audiofile
        recorder = sr.Recognizer()
        in_audio = sr.AudioFile(audiofile)

        with in_audio as source:
            raudio = recorder.record(source)
            recorder.adjust_for_ambient_noise(source)
            try:
                textdata = recorder.recognize_google(raudio,language='en-IN')
            except:
                textdata = "None"
        
        return textdata

    


if __name__ == "__main__":

    cs = ConvertToText(sys.argv[1])
    print(cs.convertotext())





    