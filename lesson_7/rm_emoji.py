#!/usr/bin/python3
import re


def remove_emoji(text):
    return re.sub(pattern=r'\p{Emoji}', repl='', string=text)