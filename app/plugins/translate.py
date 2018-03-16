# -*- coding: utf-8 -*-$

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from google.cloud import translate
import logging
import re
# Imports the Google Cloud client library$

logger = logging.getLogger(__name__)


REGEX_HELP = 'help$'


def is_help(message):
    m = re.compile(REGEX_HELP, re.IGNORECASE)

    if m.match(message) is None:
        return False
    else:
        return True


@respond_to('\S')
@listen_to('\S')
def default_func(message):

    text_value = message._body.get("text")

    if is_help(text_value):
        help_func(message)
        return

    translate_client = translate.Client()

    source_result = translate_client.detect_language(text_value)

    source_language = source_result.get("language", "en")

    logger.info("source_language: {}".format(source_language))

    target = "en"

    if source_language == "ja":
        target = 'en'

    elif source_language == "en":
        target = "ja"

    translation = translate_client.translate(text_value, target_language=target)

    message.reply_webapi(text=" ", attachments=[{'text': translation.get("translatedText")}, ])

    logger.info(message._body.get("text"))


def help_func(message):

    message.send("""このbotでは「日本語から英語」、「英語から日本語」の変換ができます。またその他の言語は「英語」に変換されます。また、サポートしている言語は以下の通りです。
    I help you to convert Japanese to English or English to Japanese. Other languages convert to English. Supported languages are below.""")

    """Lists all available lianguages."""
    translate_client = translate.Client()

    results = translate_client.get_languages()

    result_languages = ""
    for language in results:
        result_languages = result_languages + u'{name} ({language})'.format(**language) + ", "

    message.send(result_languages)
