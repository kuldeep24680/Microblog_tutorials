import json
from flask_babel import _
from app import app
import boto3

def translate(text,source_language, dest_language):
    if not app.config['SECRET_KEY'] and not app.config['ACCESS_KEY']:
        return _('Error: the translation service is not configured. ')
    translate = boto3.client(service_name='translate', aws_access_key_id=app.config['ACCESS_KEY'],aws_secret_access_key=app.config['SECRET_KEY'],region_name='us-east-1', use_ssl=True)
    #translate = boto3.client(service_name='translate', aws_access_key_id='AKIAJVCT74UCHZSD6MSA',aws_secret_access_key='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',region_name='us-east-1', use_ssl=True)

    result = translate.translate_text(Text=text,
            SourceLanguageCode=source_language, TargetLanguageCode=dest_language)
    if result['ResponseMetadata']['HTTPStatusCode']!=200:
        return _('Error: the translation service failed.')
    return result.get('TranslatedText')



