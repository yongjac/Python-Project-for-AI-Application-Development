"""This module uses IBM Watson Language Translation API to translate languages"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

URL_LT='https://api.us-south.language-translator.watson.cloud.ibm.com/instances'\
       '/dc2ac109-59fa-497f-9588-8c4948111828'
APIKEY_LT='57wAHd_sPdkzb7KlcpBDO048JJLG8WsTqtacAtk52jxJ'
VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(URL_LT)

def english_to_french(english_text):
    """This function translate english to french"""
    if not english_text:
        return ''
    translation = language_translator.translate(text=english_text ,model_id='en-fr').get_result()
    list1 = list(translation.items())
    french_translation = list1[0][1][0]['translation']
    return french_translation

def english_to_german(english_text):
    """This function translate english to german"""
    if not english_text:
        return ''
    translation = language_translator.translate(text=english_text ,model_id='en-de').get_result()
    list1 = list(translation.items())
    german_translation = list1[0][1][0]['translation']
    return german_translation
