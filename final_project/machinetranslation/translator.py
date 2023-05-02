'''implements a translator that translate english/french to french/english
'''

import os
#import json
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=IAMAuthenticator(apikey)
)
translator.set_service_url(url)

def english_to_french(english_text):
    '''translate the specified english text to french
    '''
    translated_text = translator.translate(
        text = english_text,
        model_id ='en-fr').get_result()
    french_text = translated_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''translate the specified french text to english
    '''
    translated_text = translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translated_text['translations'][0]['translation']
    return english_text

def main():
    '''test translation methods'''

    french_text = english_to_french('Hello')
    print("ft =", french_text)

    english_text = french_to_english('Bonjour')
    print("en =", english_text)

if __name__ == "__main__":
    main()
