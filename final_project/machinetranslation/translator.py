import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('y3c2jrQ3yxsvnjlNy0bY2045Weivr52qjZ243PUg_pI7')
language_translator = LanguageTranslatorV3(
    version='2022-01-08',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/947e9c13-980f-46e8-88cd-a79a647d0449')

def english_To_French(english_Text):
    translation= language_translator.translate(text=english_Text, model_id="en-fr").get_result()
    french_Text= translation["translations"][0]["translation"]
    return french_Text

def french_To_English(french_Text):
    translation= language_translator.translate(text=french_Text, model_id="fr-en").get_result()
    english_Text= translation["translations"][0]["translation"]
    return english_Text
