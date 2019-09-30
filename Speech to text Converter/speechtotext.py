
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import sys


class MappingLookup():
    #Mapping file to changee the words
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dictmapping = dict()
    
    def getmappingdictionary(self):
        with open('mappings.csv','r') as file:
            for line in file.readlines():
                line = line.strip()
                key,value = line.split(',')[0],line.split(',')[1]
                self.dictmapping[key] = value
        return self.dictmapping


class SplitAudioConvert():
    def __init__(self,audiofile):
        self.audiofile = audiofile
        self.returntext = []

    def ConverToText(self,audiofile):
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

    def splitinchunk(self):

        maplookup = MappingLookup()
        maplookup.getmappingdictionary()
        mapdict = maplookup.dictmapping

        pydubaudio = AudioSegment.from_wav(self.audiofile)
        audiochuks = split_on_silence(pydubaudio,min_silence_len=100, silence_thresh=-500,keep_silence=300)

        for ctr,chunk in enumerate(audiochuks):

            outfile = "temp\input{0}.wav".format(ctr)
            chunk.export(outfile,format="wav")
            parsed = self.ConverToText(outfile).strip()
            
            # if mapdict.get(parsed.lower()) is None:
            #     print(parsed)

            #self.returntext.append(mapdict.get(parsed.lower()))
            self.returntext.append(parsed)
        return self.returntext



if __name__ == "__main__":

    cs = SplitAudioConvert(sys.argv[1])
    cs.splitinchunk()
    print(cs.returntext)




    