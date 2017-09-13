# -*- coding: utf-8 -*-$

from slackbot.bot import respond_to
from slackbot.bot import listen_to
# Imports the Google Cloud client library$
from google.cloud import translate
import logging
import re


# ログを取得
logger = logging.getLogger(__name__)

# 「help」のみに当てはまる正規表現、REGEX_HELPを定義
REGEX_HELP = 'help$'


# 「help」か判定する関数（helpの場合はTrue, それ以外はFalseを返す)
def is_help(message):
    m = re.compile(REGEX_HELP, re.IGNORECASE)

    if m.match(message) is None:
        print("NONEの場合：")
        print(message)
        return False
    else:
        print("helpの場合")
        print(message)
        return True


# 「help」以外のメッセージに対して、翻訳をする関数
# 「help」の場合は使い方の関数、help_funcを呼びだす
@respond_to('\S')
@listen_to('\S')
def default_func(message):

    text_value = message._body.get("text")

# helpが入力された場合
    if is_help(text_value):
        help_func(message)
        return

    # Instantiates a client
    translate_client = translate.Client()

    source_result = translate_client.detect_language(text_value)

    source_language = source_result.get("language", "en")

    logger.info("source_language: {}".format(source_language))

    target = "en"

    # The target language$i
    if source_language == "ja":
        target = 'en'

    elif source_language == "en":
        target = "ja"

    # Translates some text into English\\
    translation = translate_client.translate(text_value, target_language=target)

    logger.info("翻訳後：{},　型：{}".format(translation, type(translation)))

    message.reply_webapi(text=" ", attachments=[{'text': translation.get("translatedText")}, ])

    logger.info(message._body.get("text"))


# 「help」が入力された場合、使いかたのメッセージを出力する関
def help_func(message):

    message.send("""このbotでは「日本語から英語」、「英語から日本語」の変換ができます。またその他の言語は「英語」に変換されます。また、サポートしている言語は以下の通りです。
    I help you to convert Japanese to English or English to Japanese. Other languages convert to English. Supported languages are below.""")

    """Lists all available lianguages."""
    translate_client = translate.Client()

    results = translate_client.get_languages()

    result_languages = ""
    for language in results:
        # message.send(u'{name} ({language})'.format(**language))
        # print(u'{name} ({language})'.format(**language))
        result_languages = result_languages + u'{name} ({language})'.format(**language) + ", "

    message.send(result_languages)
