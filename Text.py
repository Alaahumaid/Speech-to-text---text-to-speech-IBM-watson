
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('rYDomo7-fQ-yiEOvKBUFJiKt8kkaBK-XOsCUWeenM9UY')
tts = TextToSpeechV1(
    authenticator=authenticator
)


tts.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/2c2d7c75-fa4a-4da0-bdad-0531edb03ab3')


with open('./rec.mp3', 'wb') as audio_file:
     res = tts.synthesize('hello how are you nice to meet you ', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
     audio_file.write(res.content)  

print("completed!")