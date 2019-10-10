
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.websocket import RecognizeCallback,AudioSource
import json



class MyCallBack(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)
        self.transcript = ''
    def on_data(self,data):
        #print(json.dumps(data, indent=2))        
        self.transcript = (data['results'][0]['alternatives'][0]['transcript'])

    def on_error(self,error):
        print("Error {0}".format(error))

    def on_inactivity_timeout(self,error):
        print("Inactivity timeout {}".format(error))



def autenticate():
    authenticator = IAMAuthenticator('M7-pQyALVCPwqIyNPCJaNqpTx0sefSQoH7URi_my1CeH')
    speechtotext = SpeechToTextV1(authenticator=authenticator)
    speechtotext.set_service_url('https://gateway-lon.watsonplatform.net/speech-to-text/api')
    return speechtotext





def ibmspeech(inputfile):

    myallback  = MyCallBack()

    with open (inputfile , 'rb') as audiofile:
        audio_source = AudioSource(audiofile)
        speechtotext = autenticate()
        speechtotext.recognize_using_websocket(audio=audio_source,content_type='audio/wav',recognize_callback=myallback,model='en-US_BroadbandModel')
        return myallback.transcript


