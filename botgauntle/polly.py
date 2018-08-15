"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import requests


# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(profile_name="adminuser")
polly = session.client("polly")
url = 'http://18.207.128.175/get/swf/Orders/closed/timed_out/50/50'


 # Request speech synthesis
greeting = polly.synthesize_speech(Text="Loverboy. Where's Lovergirl ?", OutputFormat="mp3",VoiceId="Kendra")

def synthesizeTextToSpeech(speechToSynth):
    # Access the audio stream from the speechToSynth
    if "AudioStream" in speechToSynth:
        # Note: Closing the stream is important as the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(speechToSynth["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")

            # Open a file for writing the output as a binary stream
            with open(output, "wb") as file:
                file.write(stream.read())
                stream.close()

    else:
        # The speechToSynth didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using the platform's default player
    if sys.platform == "win32":
        os.startfile(output)
    else:
        # the following works on Mac and Linux. (Darwin = mac, xdg-open = linux).
        opener = "open" if sys.platform == "darwin" else "mpg321"
        subprocess.call([opener, output])
        # originally used xgd-open. Issue is that it won't close
synthesizeTextToSpeech(greeting)

def checkSWF(url):
    r = requests.get(url, auth=('DEMO', 'DEMO'))
    json_resp = r.json()
    status = r.json().get("Status", "")
    if status == "OK": 
        swfResp = polly.synthesize_speech(Text="There's nothing to worry about at the moment. All is clear.", OutputFormat="mp3",VoiceId="Matthew")
        synthesizeTextToSpeech(swfResp)
    else : 
        errors = r.json().get("Errors", "")
        orderErr = 0
        priceErr = 0
        lastDate = ""
        for i in range(len(errors)):
            lastDate = errors[i]["StartTime"];
            if errors[i]["Name"] == "Orders":
                orderErr += 1
            else :
                priceErr += 1
         
        swfErrResp = polly.synthesize_speech(Text='We seem to have ' + str(orderErr) + ' timed out Orders & ' + str(priceErr) + ' timed out Prices in the Inbound domain for  ' + lastDate , OutputFormat="mp3",VoiceId="Matthew")
        synthesizeTextToSpeech(swfErrResp)
    return;
checkSWF(url)