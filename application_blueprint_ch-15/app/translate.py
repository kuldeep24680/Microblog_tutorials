import json
from flask_babel import _
from flask import current_app
import boto3

def translate(text,source_language, dest_language):
    if not current_app.config['SECRET_KEY'] and not current_app.config['ACCESS_KEY']:
        return _('Error: the translation service is not configured. ')


    translate = boto3.client(service_name='translate', aws_access_key_id=current_app.config['ACCESS_KEY'],aws_secret_access_key=current_app.config['SECRET_KEY'],region_name='us-east-1', use_ssl=True)

    result = translate.translate_text(Text=text,
            SourceLanguageCode=source_language, TargetLanguageCode=dest_language)
    if result['ResponseMetadata']['HTTPStatusCode']!=200:
        return _('Error: the translation service failed.')
    return result.get('TranslatedText')



