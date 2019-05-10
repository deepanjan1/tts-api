from google.cloud import texttospeech
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tts-app-39d7690db953.json"

def createAudioFile(text):
    print(len(text))
    # decrement
    n = len(text) // 5000

    # last segment length
    i = len(text) % 5000
    print(i)

    for j in range(n+1):
        if (j < n):
            text_segment = text[(j*5000):(j+1)*5000]
            googleTTSAPICall(text_segment, j)
        else:
            # use the i value for the end of the string
            text_segment = text[(j*5000):(i+5000)]
            googleTTSAPICall(text_segment, j)

    return('Audio content written to file "output.mp3"')


### Helper Functions ###
def googleTTSAPICall(text_segment, segment_number):
    # Instantiate client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=text_segment)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    file_name = 'output_' + str(segment_number) + '.mp3'
    # The response's audio_content is binary.
    with open(file_name, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
    return
