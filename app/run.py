# -*- coding: utf-8 -*-

import logging
from slackbot.bot import Bot


logging.basicConfig(level=logging.DEBUG)


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    print('start botForSlack')

    main()
