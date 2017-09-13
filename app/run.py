# -*- coding: utf-8 -*-

import logging
from slackbot.bot import Bot
from os import environ

logging.basicConfig(level=environ.get("LOG_LEVEL"))


print(environ.get("LOG_LEVEL"))


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    print('start slack-bot')

    main()
