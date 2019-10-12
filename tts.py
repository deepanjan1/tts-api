from google.cloud import texttospeech
import os

# for mp3 concatenation
from pydub import AudioSegment

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tts-app-39d7690db953.json"

def createAudioFile(text, audio_key):
    # decrement
    n = len(text) // 5000

    # iterate through each 5000 character segment due to Google API limit
    # and create separate audio files
    filenames = []

    if (n > 0):
        for j in range(n+1):
            if (j < n):
                text_segment = text[(j*5000):(j+1)*5000]
                filenames.append(googleTTSAPICall(text_segment, j))
            else:
                text_segment = text[(j*5000):]
                filenames.append(googleTTSAPICall(text_segment, j))

        # if there are more than one segment, combine all of the audio segments
        name = audioCombine(filenames, audio_key)

    else:

        # if there's just one segment, then create final output mp3
        name = googleTTSAPICall(text, n, audio_key)

    print(f"Audio content written to file '{audio_key}.mp3'")
    return(name)


### Helper Functions ###
def googleTTSAPICall(text_segment, segment_number, audio_key = ''):
    ''' takes in a segment of text and the number of the segment,
    and outputs the voice file for that text segment from the Google API.'''
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

    if audio_key != '':
        file_name = f'./audio_files/{audio_key}.mp3'
    else:
        file_name = './audio_files/output_' + str(segment_number) + '.mp3'

    # The response's audio_content is binary.
    with open(file_name, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
    return file_name

def audioCombine(file_name, audio_key):
    '''if segments are larger than 5000 characters, this function is
    used to stitch all of the segments together and create one mp3 file'''

    combined_file = AudioSegment.from_mp3(file_name[0])

    for file in file_name[1:]:
        combined_file += AudioSegment.from_mp3(file)

    # export file as an mp3 with audio_key as name
    name = f'./audio_files/{audio_key}.mp3'
    combined_file.export(name, format="mp3")

    # delete segment files
    for file in file_name:
        os.remove(file)

    return name
